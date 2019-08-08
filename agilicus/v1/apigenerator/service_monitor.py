service_monitor = """
---
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
    name: {cfg[name_version]}-{cfg[name]}-api-sm
    namespace: {cfg[metadata][namespace]}
    labels:
        app: {cfg[name_version]}-{cfg[name]}
        monitoring: prometheus
spec:
    selector:
        matchLabels:
            monitoring: prometheus
    endpoints:
        - port: {cfg[port]}
          path: {cfg[monitor][path]}
          scheme: {cfg[monitor][scheme]}
          interval: {cfg[monitor][interval]}
"""
