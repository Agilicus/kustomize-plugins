## NamespaceGenerator

Given a definition like:
```
---
apiVersion: agilicus/v1
kind: NamespaceGenerator
metadata:
  name: not-used-ns
labels: []
namespaces:
  - fluent-bit
  - istio-system
addRegistrySecret: true
secret: regcred
input_secret: .dockerconfigjson
input_secret_file: secrets.enc.yaml
```

This will create the namespaces `fluent-bit` and `istio-system`.
if `addRegistrySecret` is true, a secret (`input_secret`) will
be fetched from `input_secret_file` via sops, and output as
a registry secret called `secret` (regcred above).

This may be paired with the PrivateRegistry transformer
