rbac = """
---
apiVersion: agilicus.com/v1
kind: RbacRole
metadata:
  name: {cfg[name]}-{cfg[downstream_base_host]}-whitelist
spec:
  name: '*'
  rules:
    - host: {cfg[downstream_base_host]}.__ROOT_DOMAIN__
      path: "^/.*"
      method: "*"
"""
