ingress = """
---
apiVersion: agilicus/v1
kind: IstioIngressGenerator
metadata:
  name: http-ws-{cfg[name]}-not-used
  namespace: {cfg[namespace]}
name: http-ws-{cfg[downstream_base_host]}
hostname: {cfg[downstream_base_host]}.__ROOT_DOMAIN__
issuer: letsencrypt-istio
match_routes:
  http:
    - match:
        - uri:
            prefix: /
      route:
        - destination:
            host: http-ws-{cfg[name]}
            port:
              number: 8080
"""
