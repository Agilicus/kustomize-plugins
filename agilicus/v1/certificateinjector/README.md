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
    - fakelerootx1.pem
  env:
    - name: REQUEST_CA_BUNDLE
      value: /etc/ssl/certs/fakelerootx1.pem
  dir: /etc/ssl/certs
  targets:
    - ns.name
```

This will inject a file called `fakelerootx1.pem` into /etc/ssl/certs,
coming from the (pre-existing) configMap `cert-inject`.

The environment variable REQUEST_CA_BUNDLE is also injected with 
this cert to allow the python requests package to utilize the certificate.
