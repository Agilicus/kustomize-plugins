service = """
---
apiVersion: v1
kind: Service
metadata:
  name: {cfg[name_version]}-{cfg[name]}
  namespace: {cfg[metadata][namespace]}
spec:
  ports:
    - name: http
      port: {cfg[port]}
      protocol: TCP
      targetPort: http
  selector:
    app: {cfg[name_version]}-{cfg[name]}
  type: ClusterIP
"""
