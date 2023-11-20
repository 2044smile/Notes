# ClusterIP

* 서비스는 사용자가 직접 제거하지 않는 한 삭제되지 않는다.
* 서비스는 기본적으로 자신의 클러스터 IP를 가지고 있다. [Cluster 내 접근 가능]
* 외부[External] 에서는 접근 불가
* 즉 인가된 사용자[운영자], 내부 대시보드, Pod의 서비스 상태 디버깅 용도로 사용된다.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: svc-1
spec:
  selector:
    app: pod
  ports:
    - port: 9000  # 클러스터 내부에서 '서비스'로 사용할 포트
      targetPort: 8080  # Service 객체로 전달된 요청을 'Pod'로 전달할 떄 사용하는 포트
  type: ClusterIP
```


