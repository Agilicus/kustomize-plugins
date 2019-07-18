## ImageTransformer

Take a bill-of-materials of *all* images we wish to transform,
and transform their version (and optionally name).

For example given this config:
```
---
apiVersion: agilicus/v1
kind: ImageTransformer
metadata:
  name: not-used-it
images:
  - name: X
    tag: Y
  - name: bar
    new_name: bar1
    tag: v1
```

with this input:
```
---
apiVersion: batch/v1
kind: Job
metadata:
  name: job-1
spec:
  template:
    spec:
      containers:
      - name: foo
        image: bar
      restartPolicy: Never
```

it would result in an image tag of bar1:v1.
