#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

BASE_PAT = re.compile(r'(TOKEN|KEY|SECRET|PASS|PASSWORD|COOKIE|SESSION|AUTH|WEBHOOK|DSN)', re.I)
ID_PAT = re.compile(r'(^|_)(APP_ID|CLIENT_ID|ORG_ID|BOT_ID|TENANT_ID|WORKSPACE_ID|PROJECT_ID|TEAM_ID|USER_ID|ACCOUNT_ID|ID)($|_)', re.I)
ASSIGN_PAT = re.compile(r'^(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)=(.*)$')
CAT_PAT = re.compile(r'\$\(cat\s+([^\)]+)\)')


def is_sensitive(name: str, include_id: bool) -> bool:
    return bool(BASE_PAT.search(name) or (include_id and ID_PAT.search(name)))


def classify(rhs: str) -> tuple[str, str | None]:
    value = rhs.strip()
    cat = CAT_PAT.search(value)
    if cat:
        path = cat.group(1).strip().strip('"\'')
        if '.secrets/' in path:
            return 'secrets-file', path
        return 'file-read', path
    if value.startswith('$(') or value.startswith('"$(') or value.startswith("'$("):
        return 'command', None
    if value.startswith('$') or value.startswith('"$') or value.startswith("'$"):
        return 'reference', None
    return 'literal', None


def default_secret_path(name: str) -> str:
    return f'~/.secrets/{name.lower()}'


def audit(path: Path, include_id: bool) -> list[str]:
    rows: list[str] = []
    for lineno, raw in enumerate(path.read_text(errors='replace').splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith('#'):
            continue
        m = ASSIGN_PAT.match(line)
        if not m:
            continue
        name, rhs = m.groups()
        if not is_sensitive(name, include_id):
            continue
        mode, target = classify(rhs)
        target = target or default_secret_path(name)
        rows.append(f'{lineno}\t{name}\t{mode}\t{target}')
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description='Audit shell files for sensitive env vars without printing values.')
    parser.add_argument('shell_file', nargs='?', default='~/.zshrc')
    parser.add_argument('--include-id', action='store_true', help='Include *_ID and similar identifiers in the audit set.')
    args = parser.parse_args()

    path = Path(args.shell_file).expanduser()
    if not path.exists():
        raise SystemExit(f'missing file: {path}')

    print('line\tname\tmode\ttarget')
    for row in audit(path, include_id=args.include_id):
        print(row)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
