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

### Volume이란
- 컨테이너 내의 디스크에 있는 파일은 임시적이며, 컨테이너에서 실행될 때 애플리케이션에 적지 않은 몇 가지 문제가 발생한다. 첫째, 컨테이너가 충돌되면, kubelet은 컨테이너를 재시작시키지만, 컨테이너는 깨끗한 상태로 시작되기 때문에 기존 파일이 유실된다. 둘째, 파드에서 컨테이너를 함께 실행할 때 컨테이너 사이에 파일을 공유해야 하는 경우가 자주 발생한다. 쿠버네티스의 볼륨은 이 두 가지 문제를 모두 해결하였다.

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

- 위와같이 실행되면 /root/.aws/ 에 PROFILE_NAME 이라는 파일이 생성된다.
- 나는 data: 안에 있는 값이 키로 인식될 줄 알았는데 볼륨 마운트를 사용할 떄는 파일명으로 사용된다는 것이 정답이였다.

