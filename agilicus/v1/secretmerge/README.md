## SecretGenerator

This is a general-purpose sops `merge into existing Secret|ConfigMap`.
Given an input which has a matching object (e.g. an existing secret),
we append new values into it.

Given an input like:

Name is matched as regex. Be aware that kustomize will likely
not have yet expanded the name (hash) so you will get 'secret' as input,
not 'secret-dddd'

```
---
apiVersion: v1
kind: Secret
metadata:
  name: secret-dgh86g5d7d
type: Opaque
---
apiVersion: agilicus/v1
kind: SecretMerge
metadata:
  name: secret-*
  namespace: default
type: Secret
secret:
  - secret
```

It will emit Secret with the required entry added:

```
---
apiVersion: v1
kind: Secret
metadata:
  name: secret-dgh86g5d7d
type: Opaque
stringData:
  - secret: my-secret
```
