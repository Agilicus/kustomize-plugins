spec = """
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: {data[name]}-{data[metadata][namespace]}-gw
  namespace: istio-system
  labels:
    app: ingressgateway
spec:
  selector:
    istio: ingressgateway
  servers: []
"""

base_server = """
    port:
      number: 443
      protocol: HTTPS
      name: https-default
    tls:
      mode: SIMPLE
      serverCertificate: "sds"
      privateKey: "sds"
      credentialName: "{secret_name}"
    hosts:
      - {data[hostname]}
"""
