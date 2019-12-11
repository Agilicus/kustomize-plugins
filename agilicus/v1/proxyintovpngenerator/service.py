service = """
---
apiVersion: v1
kind: Service
metadata:
  name: http-ws-{cfg[name]}
spec:
  type: ClusterIP
  ports:
    - name: http-web
      port: 8080
      protocol: TCP
      targetPort: http
  selector:
    app:  http-ws-{cfg[name]}
"""
