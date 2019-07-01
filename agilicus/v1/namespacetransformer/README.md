## NamespaceTransformer

This takes items with *no namespace* and sets it.
Its intended to allow for cases where e.g. you need to install
a Gateway into istio-system, but the VirtualService into
your own namespace.

See https://github.com/kubernetes-sigs/kustomize/issues/880

