
---

## 4. HANDOFF.md

```markdown
# Equinet design system — export for Claude Design import

Prepared 2026-09-23 (updated). This is a clean export of the design system
rebuilt in the Equinet Module Development project, for import into Claude
Design's **native** design system — most likely updating the existing "Equinet
Media Design System" (org default), rather than adding a new one.

## How this stays in sync

Nothing here updates automatically. Every link in this chain is a deliberate,
manual step.

1. New development work happens in the Equinet Module Development Claude.ai
   Project — a module ships, a token gets promoted, a directive gets
   resolved, an open decision gets settled.
2. In that Project, ask Claude to reconcile the change into `tokens.css` and
   `README.md`, the same way this system was built and rebuilt.
3. Drop the updated files into your local clone of this repo and push:

   ```bash
   git add -A
   git commit -m "describe what changed"
   git push
