secret = """
---
apiVersion: v1
kind: Secret
metadata:
  name: {cfg[metadata][name]}
type: {cfg[secret_type]}
"""
