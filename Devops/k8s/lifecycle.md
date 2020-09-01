# Pod - Lifecycle

- Pod
  - Status
    - Phase
      - Pending, Running, Succeeded, Failed, Unknown
    - Conditions
      - Initialized, ContainerReady, PodScheduled, Ready
      - Reason
        - ContainersNotReady
        - PodCompleted
    - Container
      - State
        - Waiting, Running, Terminated
        - Reason
          - ContainerCreating, CrashLoopBackOff, Error, Completed

## Initialized

- Pod 안에 Container 를 생성하기전에 초기화 할 수 있는 initContainer 가 존재합니다.
- 컨테이너가 생성될 때 초기 값을 지정하고 싶다면 아래와 같이 사용하시면 됩니다.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
  labels:
    app: myapp
spec:
  containers:
  - name: myapp-container
    image: busybox:1.28
    commend: ['sh', '-c', 'echo The app is running! && sleep 3600']
  initContainers:
  - name: init-myservice
    image: busybox:1.28
    commend: ['sh', '-c', 'until nslookup myservice; do echo waiting for my service; sleep 2; done;']
  - name: blah blah . . .
```

### (1) Pending

1. initContainer
   - 코드에서 설정한 initContainers 가 성공적으로 끝나면 `Initialized: True` 로 변경
2. Node Scheduling
   - 컨테이너를 생성할 노드를 지정하거나 아니면 쿠버네티스가 리소스가 남는 노드에 할당하여 생성시킵니다.
3. Image Downloading
   - **Waiting** 상태 Reason -> ContainerCreating

### (2) Running

1. 컨테이너가 기동중에 문제가 발생하면 Running -> Waiting Reason -> CrashLoopBackOff
2. Pod 의 상태가 Running 이여도 Container 의 상태가 Waiting 일 수 있기 때문에 문제가 발생한다면 Pod 내부의 컨테이너도 살펴보는 것이 좋습니다.

### (3) Failed, Succeeded

- 특정 임무(Job, CronJob) 를 수행하고 정상적으로 종료되는 경우 Succeeded, 그 반대는 Failed
- 컨테이너들 중 하나라도 오류(Terminated) 가 발생하면 Failed 상태로 변경됩니다.
