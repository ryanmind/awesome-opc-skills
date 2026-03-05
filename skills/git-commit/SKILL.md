---
name: git-commit
description: Generate and refine Git commit messages from staged or unstaged changes. Use when the user asks for a commit message, wants type/scope/module selection, or needs messages aligned with feat/fix/refactor/docs/style/test/chore with Conventional Commits as the primary format.
---

# Git Commit

## Workflow

1. **Check staged changes**: Execute `git diff --cached` first.
2. **Fallback to unstaged**: If no staged changes, execute `git diff` and inform user.
3. **No changes**: If both empty, inform user and stop.
4. **Learn repo patterns**: Execute `git log --oneline -20 --format="%s"` to understand existing commit style.
5. **Analyze changes**: Review diff to determine change intent and affected components.
6. **Infer type**: Match change intent to type (feat/fix/refactor/docs/style/test/chore).
7. **Infer scope**: Derive from file paths and repo patterns, omit if ambiguous.
8. **Generate message**: Output concise, human-written message matching repo style.

## Message Rules

- Allowed `type`: `feat`, `fix`, `refactor`, `docs`, `style`, `test`, `chore`.
- Primary format: `type(scope): subject` (Conventional Commits).
- Compatible format: `[Module]type: subject` only when repository convention explicitly requires it.
- Default to Chinese commit messages; switch to English when repo history or user request requires it.
- Keep subject short, specific, and action-oriented:
  - Chinese: prefer <= 30 characters
  - English: prefer <= 50 characters
- Avoid trailing period in subject.
- Match repository language/style when obvious from history.

## Type Selection Heuristics

- `feat`: new user-visible behavior or capability.
- `fix`: bug fix or regression fix.
- `refactor`: internal restructuring without behavior change.
- `docs`: documentation-only changes.
- `style`: formatting/lint-only changes, no logic change.
- `test`: test-only additions or updates.
- `chore`: tooling, dependency, config, or maintenance work.

## Scope/Module Selection

**Priority order:**
1. **Learn from history**: Check recent commits for existing scope patterns.
2. **Multi-module repos**: Use top-level directory (e.g., `api`, `web`, `mobile`, `admin`).
3. **Single-module repos**: Use feature area (e.g., `auth`, `payment`, `order`, `ui`).
4. **Cross-cutting changes**: Omit scope if multiple unrelated areas are affected.
5. **When uncertain**: Omit scope rather than guessing.

**Module format `[Module]type:`**: Only use when repo history consistently shows this pattern.

## Output Patterns

- **Default**: Provide 1 best message (subject only for simple changes).
- **If user asks for options**: Provide 3 alternatives with different type/scope emphasis.
- **If user asks for commit body**: Return subject + blank line + bullet points (use `-` prefix).
- **Auto-suggest body when**: Changes are complex, affect multiple areas, or need explanation.
- **Footer lines**: Add when relevant (e.g., `Refs: #123`, `BREAKING CHANGE: ...`).
- **Language**: Default to Chinese; switch to English if repo history or user requires it.
- **Insufficient context**: Ask for missing information instead of guessing.

## When to Add Commit Body

**Add body when:**
- Multiple related changes in one commit
- Need to explain "why" not just "what"
- Technical trade-offs or design decisions
- Breaking changes or migration steps
- Complex refactoring with multiple steps

**Skip body when:**
- Simple single-line fix or addition
- Self-explanatory changes (e.g., `docs: fix typo`)
- Small scope with obvious intent

**Example with body:**
```
refactor(api): migrate from REST to GraphQL

- Reduce over-fetching by 60%
- Enable client-side caching with Apollo
- Maintain backward compatibility via REST adapter
- Migration guide: docs/graphql-migration.md
```

```
fix(order): fix amount calculation when discount applied

- Handle edge case when multiple discounts stack
- Add validation for negative amounts
- Update test cases for discount scenarios
```

## Examples

**Good commits (Chinese):**
```
feat(auth): 新增微信登录
fix(api): 修复订单查询超时
refactor: 重构用户服务层
docs: 更新 API 文档
chore(deps): 升级 React 到 18.3
```

**Good commits (English):**
```
feat(auth): add WeChat login
fix(api): fix order query timeout
refactor: restructure user service layer
docs: update API documentation
chore(deps): upgrade React to 18.3
```

**Bad commits (avoid):**
```
更新代码                           # Too vague
feat: 添加了一些新功能并修复了bug    # Mixed types
Fix bug.                          # Has trailing period, not descriptive
feat(auth): 实现了用户登录功能。   # Has trailing period, sounds like AI
```

## Human-Written Style

**Avoid AI patterns (Chinese):**
- ❌ "实现了..."、"完成了..."、"进行了..." (sounds like status report)
- ✅ "新增..."、"修复..."、"重构..."、"更新..." (action-oriented)

**Avoid AI patterns (English):**
- ❌ "implemented...", "completed...", "performed..." (sounds like status report)
- ✅ "add...", "fix...", "refactor...", "update..." (action-oriented)

**Keep it concise:**
- ❌ `feat(auth): 实现了用户通过微信扫码进行第三方登录的功能`
- ✅ `feat(auth): 新增微信扫码登录`
- ❌ `feat(auth): implemented user authentication via WeChat QR code scanning`
- ✅ `feat(auth): add WeChat QR login`

**Be specific:**
- ❌ `fix: 修复问题` / `fix: fix issue`
- ✅ `fix(order): 修复折扣叠加时的金额计算错误`
- ✅ `fix(order): fix amount calculation when discount applied`
- ✅ `fix(api): 处理用户查询返回 null 的情况`
- ✅ `fix(api): handle null response in user query`
- ✅ `feat(auth): 新增 OAuth2 token 刷新逻辑`
- ✅ `feat(auth): add OAuth2 token refresh logic`
- ✅ `refactor(db): 从 callback 迁移到 async/await`
- ✅ `refactor(db): migrate from callbacks to async/await`
- ✅ `chore(deps): 升级 axios 修复安全漏洞`
- ✅ `chore(deps): upgrade axios to fix security vulnerability`
- ✅ `test(auth): 新增登录流程单元测试`
- ✅ `test(auth): add unit tests for login flow`
- ✅ `docs(api): 新增分页参数示例`
- ✅ `docs(api): add examples for pagination params`
