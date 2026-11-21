---
type: Playbook
title: Staging health check
description: Verify service health after a staging rollout.
---

# Staging health check

This example uses a fictional service. When adapting it, link the service README and rollout workflow that own the endpoint and revision.

1. Use the staging health endpoint listed in the service README.
2. Record the rollout revision and check for HTTP 200. Compare the revision with the rollout record.
3. If the check fails, record the status and expected revision and hand those details to the on-call engineer.

## Expected result

The health endpoint returns HTTP 200 and the running revision matches the rollout record.
