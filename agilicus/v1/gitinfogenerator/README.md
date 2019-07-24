## GitInfoGenerator

Given an instantiation (no arguments are needed):

```
---
apiVersion: agilicus/v1
kind: GitInfoGenerator
metadata:
  name: not-used-gig
```

Results in a ConfigMap as:

```
---
apiVersion: v1
data:
- git-tag: 3160c647c09774c5d9eeaf4e3ba27045a7176c1d
- applied-on: '2019-07-24T13:40:51.997949'
- applied-by: don
kind: ConfigMap
metadata:
  name: deployment-info
  namespace: default
```
