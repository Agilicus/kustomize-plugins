## PrivateRegistry

Given a transformer input like:

```
---
apiVersion: agilicus/v1
kind: PrivateRegistry
metadata:
  name: not-used-pr
secret: regcred
input_secret: .dockerconfigjson:
input_secret_file: secrets.enc.yaml
```

this will _transform_ all Deployment/DaemonSet/StatefulSet/ReplicaSet/CronJob
such that they have an imagePullSecret of 'name: regcred'. Each namespace
that has one or more transformations will have a secret emitted,
using the value _.dockerconfigjson_ from [sops](https://github.com/mozilla/sops)
in `secrets.enc.yaml` as:

```
---
apiVersion: v1
kind: Secret
metadata:
  name: regcred
  namespace: <NAMESPACE>
type: kubernetes.io/dockerconfigjson
data:
  .dockerconfigjson: <SOMEBASE64>
```
