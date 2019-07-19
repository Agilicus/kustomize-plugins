## ApiGenerator

Given an input file like below, create a Deployment, Service, VirtualService, and Database CRD.

```
---
apiVersion: agilicus/v1
kind: ApiGenerator
metadata:
  name: not-used-api
  namespace: api
name: applications
image: cr.agilicus.com/platform/applications
port: 5006
replicas: 2
versions: 
  - v1
  - v2
env:
  - FLUENT_HOST: forward.fluent-bit
  - ACCESS_TOKEN_PUB_KEY: ${sops:ACCESS_TOKEN_PUB_KEY}
  - APPDB: ${sops:APPDB}
db:
  name: applications
  user: applications
  password: ${sops:dbpass}
```