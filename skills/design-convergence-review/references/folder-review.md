# Folder Review

Read this file only when the target is a folder or multiple related files.

1. Build a recursive design-set inventory before reviewing details.
2. Include Markdown, text, AsciiDoc, reStructuredText, PDF, Word, and parseable diagram-source files when supported by available tools.
3. Exclude hidden directories, version-control metadata, dependency folders, build output, binary assets, and user-provided exclusion patterns by default.
4. Prioritize likely entry files such as `README`, `index`, overview, architecture, design, spec, ADR, and manifest files.
5. Do not declare a file authoritative from its name alone. Establish authority from explicit statements, references, or user context.
6. Classify each relevant file by path, purpose, coverage, incoming references, outgoing references, and declared authority.
7. List uncertain or excluded files with the reason instead of silently omitting them.
8. Identify relationships among requirements, overviews, architecture, module designs, interfaces, data models, flows, ADRs, tests, and acceptance documents.
9. Review each document internally, then review cross-document coverage, authority, duplication, references, versions, and contradictions.
10. Keep the requested folder as the design-set boundary by default. Treat relevant parent or sibling documents as external evidence only; do not silently expand them into the reviewed set.
11. When the set is too large to read completely, prioritize entry files and documents on the traceability chain, list every unread file as not reviewed, and report coverage as partial in the Review Basis. Never silently sample or skip.
