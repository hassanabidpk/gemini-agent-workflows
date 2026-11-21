# Set up and review OKF docs

1. Use [the example bundle](../docs/okf/index.md) as a starting point. Put the index and first runbook under `docs/okf/` in your repo. The index links the files and declares the bundle version. Each ordinary concept file has YAML frontmatter with a `type`.
2. Point your repo’s `AGENTS.md` to the index. Replace the example runbook with your own environment, prerequisites, expected result and escalation path. Link the implementation that owns each command. Review doc updates with the code they describe. [OKF v0.3 specification](https://github.com/open-knowledge-format/open-knowledge-format/blob/main/SPEC.md)
3. For one runbook, use `/review-runbook docs/okf/staging-health-check.md` in CLI or desktop. For the whole bundle, copy [review-okf.py](review-okf.py) to the target repo and run the prompt below in either Antigravity surface. Review the proposed script and the results. [Dynamic Workflows](https://antigravity.google/docs/dynamic-workflows/)

```text
/run-workflow Run workflows/review-okf.py
```

The script first inventories indexed runbooks. A second phase reviews those files against repo sources and reports concrete mismatches and unknowns. It uses the conversation's model. Choose Hydrogen for a small bundle or Neon when the sources span several components.
