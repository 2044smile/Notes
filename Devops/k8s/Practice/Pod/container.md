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
