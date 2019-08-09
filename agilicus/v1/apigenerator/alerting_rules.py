alerting_rules = """
---
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  labels:
    alertmanager: main
    prometheus: main
    role: alert-rules
  name: {cfg[name_version]}-{cfg[name]}-api-rules
spec:
  groups:
    - name: alerts
      rules:
        - alert: {cfg[name_version]}-{cfg[name]} 5xx Errors
          expr: 'sum(flask_http_request_total{{service="{cfg[name_version]}-{cfg[name]}",status=~"5.."}}) - sum(flask_http_request_total{{service="{cfg[name_version]}-{cfg[name]}",status=~"5.."}} offset 1m) > 0'
          for: 1m
          labels:
            severity: warning
          annotations:
            summary: "API Service {cfg[name_version]}-{cfg[name]} experiencing 5xx errors"
        - alert: {cfg[name_version]}-{cfg[name]} high 5xx Errors
          expr: 'sum(flask_http_request_total{{service="{cfg[name_version]}-{cfg[name]}",status=~"5.."}}) - sum(flask_http_request_total{{service="{cfg[name_version]}-{cfg[name]}",status=~"5.."}} offset 1m) > 10'
          for: 1m
          labels:
            severity: critical
          annotations:
            summary: "API Service {cfg[name_version]}-{cfg[name]} experiencing a high number of 5xx errors"
        - alert: {cfg[name_version]}-{cfg[name]} 401 Errors
          expr: 'sum(flask_http_request_total{{service="{cfg[name_version]}-{cfg[name]}",status="401"}}) - sum(flask_http_request_total{{service="{cfg[name_version]}-{cfg[name]}",status="401"}} offset 1m) > 20'
          for: 1m
          labels:
            severity: warning
          annotations:
            summary: "API Service {cfg[name_version]}-{cfg[name]} experiencing 401 errors"
        - alert: {cfg[name_version]}-{cfg[name]} 403 Errors
          expr: 'sum(flask_http_request_total{{service="{cfg[name_version]}-{cfg[name]}",status="403"}}) - sum(flask_http_request_total{{service="{cfg[name_version]}-{cfg[name]}",status="403"}} offset 1m) > 20'
          for: 1m
          labels:
            severity: warning
          annotations:
            summary: "API Service {cfg[name_version]}-{cfg[name]} experiencing 403 errors"
        - alert: {cfg[name_version]}-{cfg[name]} not meeting response time SLA
          expr: '0 < sum(rate(flask_http_request_duration_seconds_bucket{{le="0.5",job="{cfg[name_version]}-{cfg[name]}",path!="/healthz"}}[5m])) / sum(rate(flask_http_request_duration_seconds_count{{job="{cfg[name_version]}-{cfg[name]}",path!="/healthz"}}[5m])) < 0.95'
          for: 5m
          labels:
            severity: warning
          annotations:
            summary: "API {cfg[name_version]}-{cfg[name]} is not meeting the SLA requirement of 95% of all requests within 500ms"
"""
