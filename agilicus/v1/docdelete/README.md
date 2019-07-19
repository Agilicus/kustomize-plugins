## DocDelete

Delete documents from a tree. You can specify:

- apiVersion + kind: all documents of this type are deleted.
- apiVersion + kind + name: all documents of this type and name (regardless of namespace) are deleted.
- apiVersion + kind + namespace: all documents of this type in a namespace (regardless of name) are deleted.
- apiVersion + kind + name namespace: the specific document is deleted.

```
---
apiVersion: agilicus/v1
kind: DocDelete
metadata:
  name: not-used-doc-delete
delete: 
  - apiVersion: agilicus/v1
    kind: RbacRole
  - apiVersion: agilicus/v1
    kind: RbacRole
    name: foo
  - apiVersion: agilicus/v1
    kind: RbacRole
    name: foo1
    namespace: bar
  - apiVersion: agilicus/v1
    kind: RbacRole
    namespace: bar1
```
