deployment = """
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {cfg[name_version]}-{cfg[name]}
  namespace: {cfg[metadata][namespace]}
spec:
  replicas: {cfg[replicas]}
  selector:
    matchLabels:
      app: {cfg[name_version]}-{cfg[name]}
  template:
    metadata:
      labels:
        app: {cfg[name_version]}-{cfg[name]}
      annotations:
        fluentbit.io/parser: "json"
    spec:
      affinity:
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            - labelSelector:
                matchLabels:
                  app: {cfg[name_version]}-{cfg[name]}
              topologyKey: kubernetes.io/hostname
      imagePullSecrets:
        - name: regcred
      containers:
        - name: {cfg[name]}
          image: {cfg[image]}
          imagePullPolicy: Always
          ports:
            - containerPort: {cfg[port]}
              name: http
          env: []
          envFrom:
            - secretRef:
                name: {cfg[name_version]}-{cfg[name]}-{cfg[hash]}
          livenessProbe:
            httpGet:
              path: /healthz
              port: http
            timeoutSeconds: 2
            failureThreshold: 2
            initialDelaySeconds: 10
            periodSeconds: 30
          readinessProbe:
            httpGet:
              path: /healthz
              port: http
            initialDelaySeconds: 10
            periodSeconds: 2
            timeoutSeconds: 2
            failureThreshold: 2
          resources:
            limits:
              memory: "400Mi"
            requests:
              memory: "200Mi"
          securityContext:
            readOnlyRootFilesystem: true
            runAsNonRoot: true
            runAsUser: 1000
            capabilities:
              drop:
                - all
          volumeMounts:
            - mountPath: /tmp
              name: tmpdir
      volumes:
        - name: tmpdir
          emptyDir:
            medium: Memory
"""
