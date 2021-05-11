poddisruptionbudget = """
---
apiVersion: policy/v1beta1
kind: PodDisruptionBudget
metadata:
  name: {cfg[name_version]}-{cfg[name]}
  namespace: {cfg[metadata][namespace]}
spec:
  minAvailable: 1
  selector:
    matchLabels:
      app: {cfg[name_version]}-{cfg[name]}
"""
