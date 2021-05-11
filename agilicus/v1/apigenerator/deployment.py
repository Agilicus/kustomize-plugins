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
        cluster-autoscaler.kubernetes.io/safe-to-evict: "true"
    spec:
      topologySpreadConstraints:
        - maxSkew: 1
          topologyKey: topology.kubernetes.io/zone
          whenUnsatisfiable: DoNotSchedule
          labelSelector:
            matchLabels:
              app: {cfg[name_version]}-{cfg[name]}
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
              path: {cfg[liveness_path]}
              port: http
            timeoutSeconds: 2
            failureThreshold: 2
            initialDelaySeconds: 10
            periodSeconds: 30
          readinessProbe:
            httpGet:
              path: {cfg[readiness_path]}
              port: http
            initialDelaySeconds: 10
            periodSeconds: 2
            timeoutSeconds: 2
            failureThreshold: 2
          resources:
            limits:
              memory: "{cfg[mem_limit]}"
            requests:
              memory: "{cfg[mem_request]}"
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
