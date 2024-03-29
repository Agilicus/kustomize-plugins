dest_rule = """

apiVersion: networking.istio.io/v1alpha3
kind: DestinationRule
metadata:
  name: {cfg[name_version]}-{cfg[name]}-api-dr
  namespace: {cfg[metadata][namespace]}
spec:
  host: {cfg[name_version]}-{cfg[name]}.{cfg[metadata][namespace]}.svc.cluster.local
  trafficPolicy:
    outlierDetection:
      consecutiveGatewayErrors: 3
      interval: 5s
      baseEjectionTime: 2s
      maxEjectionPercent: 50
    connectionPool:
      tcp:
        connectTimeout: 1500ms
"""
