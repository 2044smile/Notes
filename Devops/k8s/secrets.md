# Copying Kubernetes Secrets Between Namespaces

```
kubectl get secrets target --namespace=A --export -o yaml |\
kubectl apply --namespace=B -f -
```
    

## Reference
- https://www.revsys.com/tidbits/copying-kubernetes-secrets-between-namespaces/