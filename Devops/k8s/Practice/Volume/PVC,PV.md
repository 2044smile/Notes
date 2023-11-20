# PVC, PV

* PV (Persistent Volume)와 PVC (Persistent Volume Claim)는 클러스터 내에서 **영속적인 스토리지**를 관리하는 데 사용되는 기능입니다.

1. Persistent Volume (PV)
   - 클러스터 내에서 사용 가능한 스토리지를 나타냅니다.
   - 즉, 물리적인 스토리지 자원이나 클라우드 스토리지 등을 대표합니다.
   - **PV는 관리자가 수동으로 생성하며, 클러스터의 여러 노드에서 공유될 수 있습니다.**
   - PV는 특정 스토리지 클래스와 연결되어 어떤 종류의 스토리지를 제공하는지 정의할 수 있습니다.
2. Persistent Volume Claim (PVC)
   - 애플리케이션에서 스토리지에 대한 요청을 나타냅니다.
   - 즉, PV를 동적으로 할당하려는 의도를 나타냅니다.
   - **PVC는 개발자 또는 애플리케이션에서 생성되며, 특정 스토리지 클래스와 요청하는 스토리지 용량을 정의합니다.**
   - 클레임이 접근하려는 스토리지 클래스가 없으면 클러스터에서 설정된 기본 스토리지 클래스를 사용합니다.
   - PVC는 PV에 바인딩되어 특정 PV와 매칭됩니다. 이렇게 함으로써 PVC에 필요한 스토리지를 동적으로 할당하고 해제할 수 있습니다.

생성 순서는 아래와 같습니다.

* PV 정의 생성[User] -> PVC 생성[User] -> PV 연결[Admin] -> Pod 생성 시 PVC 마운팅[Admin][git, ISCSI, AWS, NFS]

### 아래 내용 추가 설명
* capacity[용량]: PV에서 사용 가능한 스토리지의 크기[용량]를 나타냅니다.
* accessModes: PV에 대한 액세스 모드를 정의합니다. 이는 PV에 어떻게 정의할지를 나타냅니다.
  * 예를 들어, 'ReadWriteOnce' 는 단일 노드에서 읽기와 쓰기가 가능하다는 것을 의미하며, 'ReadOnlyMany' 는 여러 노드에서 읽기만 가능하다는 것을 의미합니다.
* storageClassName: 스토리지 클래스를 지정합니다. 스토리지 클래스는 PV를 동적으로 생성할 때 사용되는 템플릿을 정의합니다. 즉, PVC 에서 요청한 스토리지를 제공하는데 사용합니다.
* local: 로컬 디스크에 PV를 생성할 때 사용되는 옵션입니다. EX] path
* nodeAffinity:: **PV를 특정 노드에 바인딩하기 위한 규칙을 정의**합니다.
```yaml
spec:
  capacity:
    storage: 1Gi
---
spec:
  accessModes:
    - ReadWriteOnce
---
spec:
  storageClassName: "standard"
---
spec:
  local:
    path: "/mnt/data"
---
nodeAffinity:
    required:
      nodeSelectorTerms:
      - matchExpressions:
        - {key: kubernetes.io/hostname, operator: In, values: [k8s-node1]}
```

## PV

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-01
spec:
  capacity:  # 용량
    storage: 1G
  accessModes:
  - ReadWriteOnce
  local:
    path: /node-v
  nodeAffinity:
    required:
      nodeSelectorTerms:
      - matchExpressions:
        - {key: kubernetes.io/hostname, operator: In, values: [k8s-node1]}
---
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-02
spec:
  capacity:
    storage: 1G
  accessModes:
  - ReadOnlyMany
  local:
    path: /node-v
  nodeAffinity:
    required:
      nodeSelectorTerms:
      - matchExpressions:
        - {key: kubernetes.io/hostname, operator: In, values: [k8s-node1]}
---
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-03
spec:
  capacity:
    storage: 2G
  accessModes:
  - ReadWriteOnce
  local:
    path: /node-v
  nodeAffinity:
    required:
      nodeSelectorTerms:
      - matchExpressions:
        - {key: kubernetes.io/hostname, operator: In, values: [k8s-node1]}
```

## PVC

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-01
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 1G  # PV-01과 연결
  storageClassName: ""
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-02
spec:
  accessModes:
  - ReadOnlyMany
  resources:
    requests:
      storage: 1G
  storageClassName: ""
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-03
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 3G  # PV-03과 연결 시도 but 3G를 요구 했고, PV-03 은 2G 다.
  storageClassName: ""
# 연결이 되지 않는다.
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-04
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 1G  # PV-03과 연결
  storageClassName: ""
```
