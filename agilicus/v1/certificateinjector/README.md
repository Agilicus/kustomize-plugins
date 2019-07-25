## CertificateInjector

Given a definition like:

```
---
apiVersion: agilicus/v1
kind: CertificateInjector
metadata:
  name: not-used-cert-inject
inject:
  configMap: cert-inject
  certs:
    - fakelerootx1.pem:
  dir: /etc/ssl/certs
  targets:
    - ns.name
```

This will inject a file called `fakelerootx1.pem` into /etc/ssl/certs,
coming from the (pre-existing) configMap `cert-inject`.
