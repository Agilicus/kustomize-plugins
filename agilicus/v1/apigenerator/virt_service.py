virt_service = """
---
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: {cfg[name_version]}-{cfg[name]}-api-vs
  namespace: {cfg[metadata][namespace]}
spec:
  hosts:
    - api.__ROOT_DOMAIN__
  gateways:
    - istio-system/api-gw
  http:
    - match: []
      headers:
        response:
          set:
            Strict-Transport-Security: max-age=63072000; includeSubDomains
          remove:
            - x-envoy-upstream-service-time
      route:
        - destination:
            host: {cfg[name_version]}-{cfg[name]}.{cfg[metadata][namespace]}.svc.cluster.local
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
          - authorization
          - content-type
        maxAge: "24h"
"""
