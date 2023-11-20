# hostPath

* **노드의 파일 시스템 경로**를 파드 내의 컨테이너에 마운트 할 때 사용합니다.
* 주로 디버깅이나 특수한 상황에서 사용되며, 'hostPath' 를 사용하면 노드의 파일 시스템에 직접 접근할 수 있습니다. 다만 주의할 점은 파드가 어떤 노드에서 실행되느냐에 따라 실제로 마운트되는 디렉토리가 달라진다는 것 입니다. 또한 이 방법은 클러스터 간 이식성을 감소시킬 수 있고 보안상의 이유로 권장되지 않습니다.
* 즉, **노드에 있는 데이터를 파드에서 사용하는 용도이다.**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: test-pod
spec:
  containers:
  - name: container-1
    image: nginx
    volumeMounts:
    - name: hostpath-vol
      mountPath: /usr/share/nginx/html
  volumes:
  - name: hostpath-vol
    hostPath:
      path: /var/www/html
```

* **파드 내의 컨테이너에서 '/usr/share/nginx/html' 경로에 접근하는 것이 노드의 '/var/www/html' 에 접근하는 것과 동일해집니다.**
