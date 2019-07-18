service = """
---
apiVersion: v1
kind: Service
metadata:
  name: {cfg[name]}
  namespace: api
spec:
  ports:
    - name: http
      port: {cfg[port]}
      protocol: TCP
      targetPort: http
  selector:
    app: {cfg[version]}-{cfg[name]}
  type: ClusterIP
"""
