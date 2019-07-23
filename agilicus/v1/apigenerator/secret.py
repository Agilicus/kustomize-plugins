secret = """
---
apiVersion: v1
kind: Secret
metadata:
  name: {cfg[name_version]}-{cfg[name]}-{cfg[hash]}
  namespace: {cfg[metadata][namespace]}
type: Opaque
stringData: []
"""
