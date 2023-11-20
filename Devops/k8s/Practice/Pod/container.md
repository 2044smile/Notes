# Container

* 컨테이너들끼리 포트는 중복될 수 없다.
* Pod 에는 IP 자동할당 되고, 재생성 시 변경된다.
  * 외부에서는 Pod 의 IP 로 접근할 수 없다.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-1
spec:
	containers:
	- name: container-1
		image: tmkube/p8000
	  ports:
		- containerPort: 8000
	- name: container-2
		image: tmkube/p8080
		ports:
		- containerPort: 8080
```

## Label
* 파드 뿐만 아니라 모든 Object 에 달 수 있다.
* 사용 목적에 따라 Label 등록
* Object 들을 분류하고, 분류 된 Object 들만 따로 작업할 수 있다.
* Key: Value, Pod 에는 여러 개의 Label 을 달 수 있다.

**즉, Label 은 모든 Object 를 분류해서 조직화 할 수 있는 기능이다.**

```yaml
# pod1
type: web
lo: dev
# pod2
type: db
lo: dev
# pod3
type: server
lo: dev
# pod4
type: web
lo: production
# pod5
type: db
lo: production
# pod6
type: server
lo: production
```

* 웹 개발자가 web만 보고 싶다고 하면, type이 web으로 설정되어 있는 것들을 Service 로 연결해서 Open 해주면 웹 개발자가 볼 수 있다.

```yaml
apiVersion: v1
kind: Service
metadata: 
  name: svc-1
spec:
  selector:
    type: web
	ports:
		- port: 8080
---
apiVersion: v1
kind: Pod
metadata:
	name: pod-1
	labels:
		type: web
		lo: dev
spec:
	containers:
	- name: container
		image: tmkube/init
```

### Check a Label
* --show-labels 를 통해 Pod에 부착되어 있는 Label 을 확인 할 수 있다.
* -L 을 통해 특정 레이블로 이루어진 Pod 를 필터링 할 수 있다.
* **라벨의 각 키는 특정 객체에 대해 고유해야 한다.**

```markdown
# Pod에 레이블 표시
root@k8s-m:~# kubectl get pod --show-labels
NAME             READY   STATUS    RESTARTS   AGE   LABELS
john-pod-label   1/1     Running   0          29s   **env=prod,tier=backend**

# Pod 특정 레이블만 관심 있는 경우
root@k8s-m:~# kubectl get pod -L tier,env
NAME             READY   STATUS    RESTARTS   AGE   TIER      ENV
john-pod-label   1/1     Running   0          44s   **backend   prod**

root@k8s-m:~# kubectl get pod -L env
NAME             READY   STATUS    RESTARTS   AGE   ENV
john-pod-label   1/1     Running   0          58s   prod
```
