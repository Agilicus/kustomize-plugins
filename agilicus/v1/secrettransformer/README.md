## SecretTransformer

Given a definition like:
```
---
apiVersion: agilicus/v1
kind: SecretTransformer
metadata:
  name: not-used-ns
source: secrets.enc.yaml
keys:
  - secret
```

and a use like:

```
---
apiVersion: v1
kind: Pod
metadata:
  name: mydep
spec:
  containers:
    - name: foo
      image: alpine
      command: ["/bin/bash"]
      args:
        - -c
        - |
          echo "Use the ${sops:secret}"
```

The result will be that `${sops:secret}` is replaced with the value
of `secret` from the `secrets.enc.yaml` file. If the (unencrypted) 
contents of `secrets.enc.yaml` were:

```
CAT: ferocious
DOG: tame
secret: my-secret
```

then the above would become `echo "Use the my-secret"`.

In the list of `keys`, if `keys` is `*`, then all secrets
are available.

E.g.

```
keys:
  - "*"
```
