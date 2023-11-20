# NodePort

* 서비스는 기본적으로 자신의 클러스터 IP 를 가지고 있다.
* **클러스터에 연결되어 있는 모든 노드에게 똑같은 포트가 할당 된다.**
* 외부[External] 에서는 어떤 노드던 간에 그 IP의 포트로 접근을 하면 서비스에 연결이 된다.
* 모든 노드에 포트가 생성된다.
* 즉, 내부망 연결, 데모나 임시 연결용으로 사용된다.

```yaml
externalTrafficPolicy: Local 
# 특정 노드 포트에 IP 로 접근을 하는 이 트래픽은 해당 노드 위에 있는 파드에게만 전송을 보낼 수 있다.

apiVersion: v1
kind: Service
metadata:
  name: svc-2
spec:
  selector:
    app: pod
  ports:
    - port: 9000  # 클러스터 내부에서 '서비스'로 사용할 포트
      targetPort: 8080  # Service 객체로 전달된 요청을 'Pod'로 전달할 떄 사용하는 포트
      NodePort: 30000  # '외부에서 접속'하기 위해 사용하는 포트
  type: NodePort
  externalTrafficPolicy: Local
---
apiVersion: v1
kind: Service
metadata:
  name: svc-2
spec:
  type: NodePort
  ports:
  - port: 9000
    targetPort: 8080
    nodePort: 30000  # 여기에서 포트를 명시적으로 설정
  selector:
    app: pod
```
