## kustomize-plugins
Various plugins for kustomize. These are ones I needed,
YMMV on how useful they are. They are all released under
Apache 2.0 license.

Install: `cp -pr agilicus ~/.config/kustomize/plugin/`

You will also need a newer version of pyyaml (5.1.2):
`pip3 install -U --user pyyaml`

(you can also install _live_, e.g. `ln -s $PWD/agilicus ~/.config/kustomize/plugin/`)

More info on the [blog](https://www.agilicus.com/kustomize-plugin-examples/) post.

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

## IstioIngressGenerator

This will auto-generate an istio VirtualService + Gateway + Certificate.
Use with cert-manager to have Istio behave the same as nginx-ingress.

## BranchRestrict

Prevent users from applying a set of yaml when not on master

## CertificateTransformer

Change all certificates to e.g. Let's Encrypt Staging

## privateregistry

Enable private registry in a namespace

## grafanadashboardgenerator

Add grafana dashboards from json

## lockcontext

Prevent operation on the wrong Kubernetes context.

## secrettransformer

Modify secrets inline w/ sops

## secretmerge

Merge secrets w/ more from sops

## secretgenerator

Create a secret from sops

## crdgenerator

Select only CRD from certain input files (for a 2-pass install using same source)

## namespacetransformer

Add namespaces

## imagetransformer

Image pins done simply.

## gitinfogenerator

Generate annotation of who applied what when, as a configmap

## certificateinjector

Add certificates

## secretstringdatatransformer

Convert base64 to string for later merging
