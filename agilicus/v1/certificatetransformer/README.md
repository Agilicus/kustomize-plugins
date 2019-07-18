## CertificateTransformer

Given a definition file like:
```
---
apiVersion: agilicus/v1
kind: CertificateTransformer
metadata:
  name: not-used-cert
name: to-staging
oldIssuer: letsencrypt-istio
newIssuer: letsencrypt-istio-staging
except:
  - istio-system/auth-certificate
```

This will take all Certificates that have the issuer `letsencrypt-istio`
and convert them to `letsencrypt-istio-staging` *except* if
the name is istio-system/auth-certificate.
