Various plugins for kustomize. 

Install: cp -pr agilicus ~/.config/kustomize/plugin/

## NamespaceGenerator

This takes a config file like:
```
---
apiVersion: agilicus/v1
kind: NamespaceGenerator
metadata:
  name: not-used
labels:
  a1: val1
  a2: val2 b
namespaces:
  - ns1
  - ns2
```

and generates the namespaces requested with the labels given.
