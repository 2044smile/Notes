# Load Balancer

* 노드 포트의 특징을 그대로 가지고 있다.
* 로드 밸런서는 각각의 노드에 통신을 분산해서 보낸다.
* 별도로 외부 접속 IP를 할당해줘야 한다. [플러그인 설치]
* 즉, 외부 시스템에 노출

```yaml
apiVersion: v1
kind: Service
metadata:
  name: svc-3
spec:
  selector:
    app: pod
  ports:
    - port: 9000
      targetPort: 8080
  type: LoadBalancer
```

* 로컬 환경에서는 생성되지 않는다.
* 외부에서 접근할 수 있도록 External IP 가 할당되어야 한다.