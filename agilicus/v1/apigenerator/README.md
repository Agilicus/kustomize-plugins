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
  - name: FLUENT_HOST
    value: forward.fluent-bit
  - name: ACCESS_TOKEN_PUB_KEY
    value: ${sops:ACCESS_TOKEN_PUB_KEY}
  - name: APPDB
    value: ${sops:APPDB}
db:
  name: applications
  user: applications
  password: ${sops:dbpass}

```

Notes:

- You can add an optional `name_version` field, it will override the prefix
of the Deployment/Service/VirtualService

- You can specify paths in the versions (e.g. v1/foo). If you do, it must
fully specify all of the endpoints. Use this if your API container is > 1 API
endpoint (e.g. if you have a container that is /v1/foo, /v1/bar, /v2/foo, you
must specify all those).

So, as an example:

```
---
apiVersion: agilicus/v1
kind: ApiGenerator
metadata:
  name: not-used-api
  namespace: api
name: applications
name_version: v1
image: cr.agilicus.com/platform/applications
port: 5006
replicas: 2
versions: 
  - users
  - v1/users
env:
  - name: FLUENT_HOST
    value: forward.fluent-bit
  - name: ACCESS_TOKEN_PUB_KEY
    value: ${sops:ACCESS_TOKEN_PUB_KEY}
  - name: APPDB
    value: ${sops:APPDB}
db:
  name: applications
  user: applications
  password: ${sops:dbpass}

```
