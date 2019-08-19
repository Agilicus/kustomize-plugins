## GrafanaDashboardGenerator

Note: this is not crucial to use, you can simply construct
a ConfigMap with a label of `grafana_dashboard=true`.

However, it has the simplicity of being able to include a list
of files and create a separate configmap for each, with that
label.

```
---
apiVersion: agilicus/v1
kind: GrafanaDashboardGenerator
metadata:
  name: istio-dashboards
  namespace: api
dashboards:
  - foo.json
  - bar.json
```
