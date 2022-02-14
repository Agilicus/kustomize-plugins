spec = """
apiVersion: networking.istio.io/v1beta1
kind: Gateway
metadata:
  name: {name}
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
      cipherSuites:
        - ECDHE-ECDSA-AES256-GCM-SHA384
        - AES256-GCM-SHA384
        - ECDHE-RSA-AES256-GCM-SHA384
        - ECDHE-RSA-CHACHA20-POLY1305
        - ECDHE-ECDSA-CHACHA20-POLY1305
        - ECDHE-RSA-CHACHA20-POLY1305
        - ECDHE-ECDSA-AES128-GCM-SHA256
        - ECDHE-RSA-AES128-GCM-SHA256
      minProtocolVersion: TLSV1_2
    hosts:
      - {data[hostname]}
"""
