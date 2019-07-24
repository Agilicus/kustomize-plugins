## SecretStringDataTransformer

Take all input secrets, if they use 'data', convert them to stringData
so that later transformer can apply.
You can apply names as 'name' or 'namespace/name' in convert or skip.
If '*' is present in convert, all (except those in skip) are converted.

```
---
apiVersion: agilicus/v1
kind: SecretStringDataTransformer
metadata:
  name: not-used-ssdt
convert:
  - "*"
skip: []
```
