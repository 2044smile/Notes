# emptyDir

* **일시적인 데이터를 공유하는 데 사용된다.**
* 파드 내의 여러 컨테이너 간에 데이터를 공유할 때 유용합니다.
* 파드가 삭제되거나, 파드의 노드가 재시작되면 'emptyDir' 에 있는 데이터는 사라지게 됩니다.
* **즉, 파드 내에서 임시로 데이터를 공유하기 위한 용도로 사용되는 볼륨**

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
    - name: shared-data
      mountPath: /data
  - name: container-2
    image: busybox
    volumeMounts:
    - name: shared-data
      mountPath: /data
  volumes:
  - name: shared-data
    emptyDir: {}
```

