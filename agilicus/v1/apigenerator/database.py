database = """
---
apiVersion: agilicus.com/v1
kind: cockroachdb
metadata:
  name: {cfg[db][name]}
  namespace: {cfg[metadata][namespace]}
spec:
  dbname: {cfg[db][db_name]}
  user: {cfg[db][user]}
  password: {cfg[db][password]}
  restore: true
  restorefrom: now
"""
