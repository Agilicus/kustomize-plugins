service = """
---
apiVersion: v1
kind: Service
metadata:
  name: {cfg[versions][0]}-{cfg[name]}
  namespace: {cfg[metadata][namespace]}
spec:
  ports:
    - name: http
      port: {cfg[port]}
      protocol: TCP
      targetPort: http
  selector:
    app: {cfg[versions][0]}-{cfg[name]}
  type: ClusterIP
"""
