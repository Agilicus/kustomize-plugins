service = """
---
apiVersion: v1
kind: Service
metadata:
  name: http-ws-{cfg[name]}
  labels:
    monitoring: http-ws-{cfg[name]}
spec:
  type: ClusterIP
  ports:
    - name: http-web
      port: 8080
      protocol: TCP
      targetPort: http
    - name: http-admin-and-health
      port: 8877
      protocol: TCP
      targetPort: admin-health
  selector:
    app:  http-ws-{cfg[name]}
"""
