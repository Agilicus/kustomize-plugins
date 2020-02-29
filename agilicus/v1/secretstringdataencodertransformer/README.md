## SecretStringDataEncoderTransformer

Take all input secrets, if they use 'stringData', convert them to data
to provide back to kustomize in a usuable structure so that suffix 
hashing can take effect.
You can apply names as 'name' or 'namespace/name' in convert or skip.
If '*' is present in convert, all (except those in skip) are converted.

```
---
apiVersion: agilicus/v1
kind: SecretStringDataEncoderTransformer
metadata:
  name: not-used-ssdt
convert:
  - "*"
skip: []
```
