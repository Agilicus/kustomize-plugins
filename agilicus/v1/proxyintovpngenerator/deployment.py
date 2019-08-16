deployment = """
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: http-ws-{cfg[name]}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: http-ws-{cfg[name]}
  template:
    metadata:
      labels:
        service: http-ws-{cfg[name]}
        app: http-ws-{cfg[name]}
      annotations:
        sidecar.istio.io/inject: "false"
    spec:
      securityContext:
        fsGroup: 2000
      containers:
        - name: http-ws-{cfg[name]}
          image: envoyproxy/envoy:v1.11.0
          resources:
            limits:
              cpu: 2
              memory: 800Mi
            requests:
              cpu: 200m
              memory: 100Mi
          imagePullPolicy: Always
          env:
            - name: LOG_LEVEL
              value: info
            - name: POD_NAME
              valueFrom:
                fieldRef:
                  fieldPath: metadata.name
            - name: POD_NAMESPACE
              valueFrom:
                fieldRef:
                  fieldPath: metadata.namespace
          command: ["envoy"]
          args:
            - "-l"
            - "$(LOG_LEVEL)"
            - "-c"
            - "/etc/envoy/envoy.yaml"
            - "--service-node"
            - "$(POD_NAME)"
            - "--service-cluster"
            - "http-ws-{cfg[name]}-$(POD_NAMESPACE)"
          securityContext:
            runAsNonRoot: true
            runAsUser: 10001
            capabilities:
              drop:
                - all
            readOnlyRootFilesystem: true
          volumeMounts:
            - mountPath: /etc/envoy
              name: config
              readOnly: true
          ports:
            - name: http
              containerPort: 8080
          livenessProbe:
            httpGet:
              path: /http-ws/v0/check_alive
              port: 8877
            initialDelaySeconds: 5
            periodSeconds: 3
          readinessProbe:
            httpGet:
              path: /http-ws/v0/check_ready
              port: 8877
            initialDelaySeconds: 5
            periodSeconds: 3
        - name: tcp-to-https
          image: gcr.io/agilicus/utilities/corkscrew-server:v0.1.0
          imagePullPolicy: Always
          ports:
            - name: backend
              containerPort: 5556
          volumeMounts:
            - name: xinetd-config
              mountPath: /opt/corkscrew/xinetd.d
              readOnly: true
        - name: https-to-ws
          image: cr.agilicus.com/utilities/local-gateway:0.5.0
          imagePullPolicy: Always
          env:
            - name: GATEWAY_URL
              value: http://vpn-gateway.vpn-gateway/{cfg[org_id]}/ws2tcp/x-proxy-host/x-connect-to-port
            - name: PORT
              value: "5001"
          volumeMounts:
            - name: tokens
              mountPath: /var/run/tokens
      volumes:
        - name: config
          configMap:
            name: {cfg[envoy_config_name]}
        - name: tokens
          secret:
            secretName: {cfg[tokens_secret]}
        - name: xinetd-config
          configMap:
            name: {cfg[xinetd_config_name]}
      restartPolicy: Always
      imagePullSecrets:
        - name: regcred
      affinity:
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
            - weight: 1
              podAffinityTerm:
                labelSelector:
                  matchExpressions:
                    - key: app
                      operator: In
                      values:
                        - http-ws-{cfg[name]}
                topologyKey: "kubernetes.io/hostname"
"""
