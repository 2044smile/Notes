# Copying Kubernetes Secrets Between Namespaces

```
kubectl get secrets target --namespace=A --export -o yaml |\
kubectl apply --namespace=B -f -
```
    

## Reference
- https://www.revsys.com/tidbits/copying-kubernetes-secrets-between-namespaces/


# 여러 개의 Secret키를 한번에 처리 

### secret.yaml 생성
```yaml
# secret.yaml

apiVersion: v1
kind: Secret
metadata:
  name: conn-secret
  namespace: {{ .Release.Namespace }}
type: Opaque
data:
  PROFILE_NAME: default
  HOSTNAME: localhost
  PORT: 5439
  USERNAME: demo
  PASSWORD: test1234
  DATABASE: demo
```

### 생성한 모든 전역에 있는 secret을 사용
```yaml
container:
  image: blah:latest
  envFrom:
  - secretRef:
      name: conn-secret
```

## Reference
- https://kubernetes.io/docs/tasks/inject-data-application/distribute-credentials-secure/

# secret 을 꺼낼 때 \n newline 오류


## Reference
- https://superuser.com/questions/1225134/why-does-the-base64-of-a-string-contain-n/1225139