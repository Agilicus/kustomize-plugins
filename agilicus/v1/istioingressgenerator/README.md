## IstioIngressGenerator

If `cookie_hash: true` then it will automatically generate
a DestinationRule with consitentHash enabled by a cookie
called `agilicus-lb`.

```
---
apiVersion: agilicus/v1
kind: IstioIngressGenerator
metadata:
  name: not-used-ingress
name: alertmanager
hostname: alertmanager.__ROOT_DOMAIN__
issuer: letsencrypt-istio
cookie_hash: true
match_routes:
  http:
    - match:
        - uri:
            prefix: /
      route:
        - destination:
            host: alertmanager-main
            port:
              number: 9093
destination:
  tls:
    mode: SIMPLE
    sni: foobar
  loadBalancer:
    consistentHash:
      httpCookie:
        name: agilicus-lb
        ttl: 0s
```
