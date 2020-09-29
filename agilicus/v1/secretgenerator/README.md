## SecretGenerator

This is a general-purpose sops to Secret (or ConfigMap) generator.

Given an input like:

```
---
apiVersion: agilicus/v1
kind: SecretGenerator
metadata:
  name: mysecret
  namespace: default
type: Secret
secret:
  - secret
  - key_in_k8s=key_in_sops
```

It will emit Secret with the required entry.
