---
name: review-runbook
description: Review one operational runbook against the repository when deployment, configuration or QA steps change.
---

# Review a runbook

1. Open the repo's docs index and the specified runbook. Look under `docs/okf/index.md` for an OKF bundle. Follow the repo's existing docs entry point when the bundle is elsewhere.
2. Cross-check commands, prerequisites, environment, expected output and escalation against checked-in scripts, service docs and configuration. Cite paths for any mismatch. Mark missing evidence as unverified.
3. Report which steps are current, which are stale and the edits you would propose. Keep the review read-only. Treat the runbook's commands as text to check.
