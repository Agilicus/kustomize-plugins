secret = """
---
apiVersion: v1
kind: Secret
metadata:
  name: {cfg[metadata][name]}
  annotations: {cfg[metadata][annotations]}
type: Opaque
stringData: []
"""
