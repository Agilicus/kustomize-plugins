## ApiGenerator

Given an input file like below, create a Deployment, Service, VirtualService, Database CRD, and Mounts.

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
mounts:
  secrets:
    - name: cert-name
      path: /cert/path/
  configMap:
    - name: configmap-name
      path: /map/path

```

Notes:

- You can add an optional `name_version` field, it will override the prefix
of the Deployment/Service/VirtualService

- You can specify paths in the versions (e.g. v1/foo). If you do, it must
fully specify all of the endpoints. Use this if your API container is > 1 API
endpoint (e.g. if you have a container that is /v1/foo, /v1/bar, /v2/foo, you
must specify all those).

-To add a secret or configmap, you can specify the path it should be mounted 
on its name

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
mounts:
  secrets:
    - name: ca-cert
      path: /etc/ssl/certs
  configMap:
    - name: config-app
      path: /etc/config


```
## OPA Sidecar

You can add an OPA Sidecar for authz by adding a policy-agent
section to the generator with enabled set to true.

E.g.

```
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
policy-agent:
  enabled: true
```

### with_request_body control
The policy-agent config as an additional configuration named "with_request_body".
By default, request body is sent to the authz opa, however, this can be
disabled via "with_request_body: false". Disabling request body is a current
workaround to limit large bodies (upload/binary) to be sent to the authz sidecar.

Note that this assumes the existence of an authz model in the working
directory of the container. The model must be named `model.yaml`.
