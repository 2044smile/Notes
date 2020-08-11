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

- echo -n "default" | base64 이런식으로 암호화를 진행하면 문제가 되지 않지만 echo deafult | base64 이런식으로 진행하면 오류가 발생함

## Reference
- https://superuser.com/questions/1225134/why-does-the-base64-of-a-string-contain-n/1225139

# secret을 volumeMounts을 이용하여 파일로 생성하기
- secret.yaml
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: connection-secret
  namespace: Example
type: Opaque
data:
  PROFILE_NAME: ZGVmYXVsdA== # echo -n "default" | base64 결과
```

- example.yaml
```yaml
container:
  image: blahblah:latest
  volumeMounts:
    - name: secret-volume
      mountPath: /root/.aws/
  envFrom:
  - secretRef:
      name: connection-secret
  command: ["python", "-m", "{{`{{inputs.parameters.wish}}`}}.{{`{{inputs.parameters.type}}`}}.{{`{{inputs.parameters.run}}`}}", "{{`{{inputs.parameters.part}}`}}", "{{`{{inputs.parameters.gender}}`}}", "{{`{{inputs.parameters.uuid}}`}}"]
volumes:
  - name: secret-volume
    secret:
      secretName: connection-secret
```
