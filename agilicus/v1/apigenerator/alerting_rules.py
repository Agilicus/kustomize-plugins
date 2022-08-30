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
  namespace: {cfg[metadata][namespace]}
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
          expr: '0 < sum(rate(flask_http_request_duration_seconds_bucket{{le="2.5",job="{cfg[name_version]}-{cfg[name]}",path!="{cfg[liveness_path]}"}}[5m])) / sum(rate(flask_http_request_duration_seconds_count{{job="{cfg[name_version]}-{cfg[name]}",path!="{cfg[liveness_path]}"}}[5m])) < 0.95'
          for: 5m
          labels:
            severity: warning
          annotations:
            summary: "API {cfg[name_version]}-{cfg[name]} is not meeting the SLA requirement of 95% of all requests within 2500ms"
        - alert: {cfg[name_version]}-{cfg[name]}  api,db connection issue
          expr: 'sum(rate(db_fail_total{{service = "{cfg[name_version]}-{cfg[name]}"}}[1m])) > 0 and  sum(rate(flask_http_request_total{{service="{cfg[name_version]}-{cfg[name]}",status=~"5.."}}[1m])) > 0'
          for: 1m
          labels:
            severity: warning
          annotations:
            summary: "API service {cfg[name_version]}-{cfg[name]}  on cluster : __CLUSTER__ because for about one minute, the db_fail_total counter has an increasing rate and the database is returning the responce code of 500"
        
        - alert: {cfg[name_version]}-{cfg[name]} high api,db connection issue 
          expr: 'sum(rate(db_fail_total{{service = "{cfg[name_version]}-{cfg[name]}"}}[1m])) > 0  and sum(rate(flask_http_request_total{{service="{cfg[name_version]}-{cfg[name]}",status=~"5.."}}[1m])) > 0'
          for: 5m
          labels:
            severity: critical
          annotations:
            summary: "API service {cfg[name_version]}-{cfg[name]} on cluster : __CLUSTER__ because for about five minutes, the db_fail_total counter has an increasing rate and the database is returning the responce code of 500 "
        - alert: {cfg[name_version]}-{cfg[name]} api cache amq connection failures
          expr: 'sum(rate(amq_manager_connection_failures_total{{service = "{cfg[name_version]}-{cfg[name]}"}}[1m])) > 0'
          for: 5m
          labels:
            severity: critical
          annotations:
            summary: "API service {cfg[name_version]}-{cfg[name]} on cluster : __CLUSTER__ the amq_manager_connection_failures_total is incrementing, which will lead to the api cache missing invalidates from amq"
        
"""
