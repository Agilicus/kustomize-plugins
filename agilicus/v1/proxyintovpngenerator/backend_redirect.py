service_entry = """
---
apiVersion: networking.istio.io/v1alpha3
kind: ServiceEntry
metadata:
  name: {cfg[name]}-backend-redirect
spec:
  hosts:
  - {cfg[upstream][host]}
  location: MESH_EXTERNAL
  ports:
  - number: 443
    name: tcp
    protocol: TLS
  resolution: DNS
"""
virtual_service = """
---
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: {cfg[name]}-backend-redirect
spec:
  hosts:
  - {cfg[upstream][host]}
  tls:
  - match:
    - port: 443
      sniHosts:
      -  {cfg[upstream][host]}
    route:
    - destination:
        host:  {cfg[name]}
"""
