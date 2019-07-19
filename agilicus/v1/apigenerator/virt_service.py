virt_service = """
---
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: {cfg[name]}-api-vs
  namespace: {cfg[metadata][namespace]}
spec:
  hosts:
    - api.__ROOT_DOMAIN__
  gateways:
    - istio-system/api-gw
  http:
    - match: []
      route:
        - destination:
            host: {cfg[versions][0]}-{cfg[name]}.api.svc.cluster.local
            port:
              number: {cfg[port]}
      corsPolicy:
        allowOrigin:
          - "*"
        allowMethods:
          - POST
          - PUT
          - DELETE
          - GET
          - OPTIONS
          - HEAD
        allowCredentials: true
        allowHeaders:
          - X-Request-ID
        maxAge: "24h"
"""
