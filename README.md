Various plugins for kustomize. 

Install: `cp -pr agilicus ~/.config/kustomize/plugin/`

(you can also install _live_, e.g. `ln -s $PWD/agilicus ~/.config/kustomize/plugin/`)

## NamespaceGenerator

This takes a config file like:
```
---
apiVersion: agilicus/v1
kind: NamespaceGenerator
metadata:
  name: not-used
labels:
  a1: val1
  a2: val2 b
namespaces:
  - ns1
  - ns2
```

and generates the namespaces requested with the labels given.

## ValueTransformer

This is a very simple `sed`. It runs over *100* of the input,
applying the sed expressions given (as OneLiner or as input file).

It takes a config file like:

```
apiVersion: agilicus/v1
kind: ValueTransformer
metadata:
  name: not-really-used
argsOneLiner: s/500.500.500.500/35.203.108.37/g
#argsFromFile: sed-input.txt
```
