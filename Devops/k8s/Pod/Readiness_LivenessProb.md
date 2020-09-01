# ReadinessProbe & LivenessProbe

## 개념

- 2개의 Pod 를 만들면 그 안에 컨테이너가 생기고 Pod, Container 상태가 Running이 되면서 Container 안에 App 은 정상적으로 구동이 됩니다.
- Service에 연결이 되고 Service 의 IP 가 외부에 알려지고, 외부에서는 해당 IP 를 보고 접속하면 사용자의 접속합니다.
- Kubernetes 는 사용자의 트래픽을 감지하여 2개의 Pod 에 적절하게 사용자의 트래픽을 할당하게 됩니다.

## CASE 1 (ReadinessProbe)

1. Pod_1, Pod_2 서로 다른 Node 에 있다고 가정하고 Pod_2 가 속한 Node 가 중지되었습니다.
2. 사용자들은 Pod_1 으로 접속하게 됩니다
3. 죽은 Pod_2 는 자동으로 다른 노드로 생성됩니다. (여기서 문제가 발생합니다.)
4. 생성되면서 사용자들은 Pod_2 가 Creating 중임에도 Kubernetes 는 Pod_2 로 사용자를 보내게됩니다. 사용자들의 반은 에러페이지를 보게되는 상황이 발생합니다.

[!] **ReadinessProbe 를 설정하게 되면 App 이 구동되는 순간에 트래픽 실패를 없애는 역할을 합니다.**

- CASE 1 에 4번 과 같은 상황일 때 적용되어 있다면 사용자들은 Pod_2가 생성되기 전 까지 Pod_1을 이용하다가 Pod_2가 생성되면 트래픽이 일부 옮겨지게 됩니다.

## CASE 2 (LivenessProbe)

1. Pod_1, Pod_2 가 정상적으로 구동하던 중 Pod_2 의 Container 안에 App 이 중지되었습니다.
2. 이 때 LivenessProbe 를 설정하게 되면 해당 App 에 문제가 생기면 Pod 를 재생성 해줍니다. 하지만 생성되면서 오는 사용자 트래픽은 에러를 보게됩니다.

## 결론

- Pod 를 생성할 때 둘 다 사용하면 좋다.
