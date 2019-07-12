## BranchRestrict

Allow the locking of use to certain branches

If remote_update is True, we do a `git remote update` and then
check `git status -uno --porcelain` is clean (empty).

```
---
apiVersion: agilicus/v1
kind: LockBranch
metadata:
  name: not-used-lb
name: lock-context
allowed_branches:
  - master
  - noc-dev
denied_branches:
  - '*'
remote_update: true
```
