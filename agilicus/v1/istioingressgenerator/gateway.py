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
        - TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
        - TLS_AES_256_GCM_SHA384
        - TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
        - TLS_CHACHA20_POLY1305_SHA256
        - ECDHE-ECDSA-CHACHA20-POLY1305
        - ECDHE-RSA-CHACHA20-POLY1305
        - TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
        - TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
      minProtocolVersion: TLSV1_2
    hosts:
      - {data[hostname]}
"""
