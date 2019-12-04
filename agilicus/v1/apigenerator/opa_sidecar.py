container="""
name: opa-istio
image: cr.agilicus.com/platform/opa-istio-plugin
imagePullPolicy: Always
args:
  - "run"
  - "--server"
  - "--log-format"
  - "json"
  - "--history"
  - "/dev/null"
  - "--config-file=/config/config.yaml"
  - "/policy/rbac_jwt_policy.rego"
  - "/policy/json.rego"
  - "/policy/json_pointer_body.rego"
  - "/policy/api_policy.rego"
  - "/config/secrets.rego"
  - "/config/static_config.rego"
  - "/model/model.yaml"
env:
  - name: JWT_SIGN_API_CERT
    valueFrom:
      secretKeyRef:
          name: {cfg[name_version]}-{cfg[name]}-{cfg[hash]}
          key: JWT_SIGN_API_CERT
  - name: GATEWAY_HOSTNAME
    value: gw.__ROOT_DOMAIN__
  - name: PORTAL_CREATOR_TOKEN
    valueFrom:
      secretKeyRef:
          name: {cfg[name_version]}-{cfg[name]}-{cfg[hash]}
          key: OPA_INTROSPECT_TOKEN
volumeMounts:
  - mountPath: "/config"
    name: "opa-config"
  - mountPath: "/model"
    name: "policy-model"
    readOnly: true
ports:
  - containerPort: 8181
    name: http
  - containerPort: 9191
    name: grpc-policy
livenessProbe:
  httpGet:
    path: /health
    port: http
  timeoutSeconds: 5
  failureThreshold: 2
  initialDelaySeconds: 61
  periodSeconds: 10
readinessProbe:
  httpGet:
    path: /health
    port: http
  initialDelaySeconds: 10
  periodSeconds: 10
  timeoutSeconds: 5
  failureThreshold: 2
securityContext:
  capabilities:
      drop:
      - all

"""
init_container = """
name: {cfg[name]}-model-init
image: {cfg[image]}
imagePullPolicy: Always
securityContext:
  readOnlyRootFilesystem: true
  runAsNonRoot: true
  runAsUser: 1000
  capabilities:
      drop:
      - all
volumeMounts:
  - mountPath: /model
    name: policy-model
command: ["cp"]
args:
  - "/web/model.yaml"
  - "/model"
"""

volumes = """
- name: "opa-config"
  configMap:
    name: cfg[opa-cfg-name]
- name: "policy-model"
  emptyDir:
    medium: Memory
"""

config = """
apiVersion: v1
kind: ConfigMap
metadata:
  name: {cfg[name_version]}-{cfg[name]}-opa-config
  namespace: {cfg[metadata][namespace]}
data:
  config.yaml: |
    plugins:
      envoy.ext_authz.grpc:
          addr: :9191
          query: data.istio.authz.allow
          log_level: trace
          fetch_static_tokens: false
          token_service_url: https://api.agilicus.com
  static_config.rego: |
    package static
    aud="urn:api:agilicus:{cfg[policy-agent][auth-name]}"
  secrets.rego: |
    package secrets
    cert = result {{
      runtime = opa.runtime()
      env = runtime["env"]
      result = env["JWT_SIGN_API_CERT"]
    }}
"""

envoy_filter = """
apiVersion: networking.istio.io/v1alpha3
kind: EnvoyFilter
metadata:
  name: {cfg[name_version]}-{cfg[name]}-ext-authz-grpc
  namespace: {cfg[metadata][namespace]}
spec:
  workloadLabels:
    app: {cfg[name_version]}-{cfg[name]}
  filters:
    - insertPosition:
        index: FIRST
      listenerMatch:
        listenerType: SIDECAR_INBOUND
        listenerProtocol: HTTP
      filterType: HTTP
      filterName: "envoy.ext_authz"
      filterConfig:
        grpc_service:
          # envoy_grpc:
          google_grpc:
            target_uri: "127.0.0.1:9191"
            stat_prefix: "ext_authz"
          timeout: 5.000s
        stat_prefix: "ext_authz"
"""
