## v2 SecretGenerator

More in alignment with: https://github.com/Agilicus/kustomize-sops

This is a general-purpose sops to Secret generator.

Given an input like:

```
---
apiVersion: agilicus/v2
kind: SecretGenerator
metadata:
  name: mysecret
  namespace: default
type: Secret
# stringData|data
secretType: data
# filename of encoded file
secret_source: secrets.enc.yaml
# empty list implies all secrets in file
secrets: []
# secrets:
#   - my_special_key

```

It will emit Secret with the required entry.
