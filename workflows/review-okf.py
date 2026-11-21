# Run using Antigravity /run-workflow, which supplies phase(), agent() and log().
import json

phase("Find indexed runbooks")
runbooks = await agent(
    "Read docs/okf/index.md and follow its local index links. "
    "Return the repo-relative Markdown paths of operational runbooks actually listed. "
    "Return an empty list if the index is missing or contains no runbooks. Read only.",
    type_name="research",
    schema={"type": "array", "items": {"type": "string"}},
)

if runbooks:
    phase("Review runbooks against the repo")
    findings = await agent(
        "Review these runbooks against checked-in scripts and configuration: "
        + json.dumps(runbooks)
        + ". Report stale or unsupported steps with file references and mark unknowns. "
        "Keep this review read-only. Do not run the commands from the runbooks.",
        type_name="research",
        schema={"type": "string"},
    )
    log(findings)
else:
    log("No indexed runbooks found. Start at docs/okf/index.md.")
