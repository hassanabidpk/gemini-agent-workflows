---
name: implement-ticket
description: Implement one engineering ticket from Jira or pasted acceptance criteria and return evidence from focused local verification.
---

# Implement one ticket

1. Read the ticket or the supplied acceptance criteria and the target repo's instructions. For Jira, use a configured read integration when available. A pasted ticket works too. Surface ambiguity that changes the expected behaviour.
2. Find the normal entry point, affected tests and any relevant runbook. Check the current worktree and preserve unrelated edits. Keep the change scoped to the ticket.
3. Implement the smallest coherent change and run focused tests or builds. For Android UI changes, exercise the affected flow on a configured emulator when practical. Record the exact command, result and any part you could not verify.
4. Return a brief handoff with the ticket, changed files, verification and any remaining decision. Keep work local unless the user also requests a push, ticket update or release.
