# One Jira ticket and focused QA

1. Open the target repo in Antigravity. Start with Hydrogen for a small, clear fix or Neon when the ticket has several moving parts.
2. Enter `/implement-ticket` followed by the Jira key or the pasted ticket. For example, “When I rotate the Android emulator on the search screen, keep the query and filters.”
3. Ask for the affected test and the expected result. With Android tooling configured, verify the flow on the emulator. Capture the device and what you observed. Review the diff and test evidence before handing it off.
4. For a cross-module change, give Argon the diff and ticket for a separate review. For an elusive bug, give Carbon the failed reproductions and ask for competing explanations and the next check that distinguishes them.

Use the target repo's build and test commands. If Jira is unavailable, paste the acceptance criteria. [Model selection](../.agents/skills/choose-gemini-model/references/models.md), [Android CLI](https://developer.android.com/tools/agents/android-cli/agent-plugins).
