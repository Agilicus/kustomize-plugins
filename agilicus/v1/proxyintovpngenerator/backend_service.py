backend_service = """
---
apiVersion: v1
kind: Service
metadata:
  name: {cfg[name]}-backend
spec:
  type: ClusterIP
  ports:
    - name: tcp-{cfg[name]}-backend
      port: 443
      protocol: TCP
      targetPort: backend
  selector:
    app: http-ws-{cfg[name]}
"""
