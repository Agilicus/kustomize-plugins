obj = """
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: http-ws-{cfg[name]}-sm
  namespace: {cfg[namespace]}
  labels:
    monitoring: prometheus
spec:
  # we want to alarm on various bits of info we attach to the deployments
  # when we create them (e.g. context like the cluster). Pass that through
  # to the metrics.
  targetLabels:
    - cluster
  selector:
    matchLabels:
      monitoring: http-ws-{cfg[name]}
  endpoints:
    - port: http-admin-and-health
      path: /http-ws/v0/metrics
      scheme: http
      interval: 5s
"""
