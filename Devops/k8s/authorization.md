# Authorization

## Service Account

- Namespace 를 생성하게 되면 default 라는 이름의 ServiceAccount 가 생성됩니다. 하지만 권한이 부여 된 상태는 아니기 때문에 다른 오브젝트에 접근하는데 제약이 있습니다.

## RBAC (Role, Rolebinding, ClusterRole)

- 클러스터롤은 특정 API나 리소스(Pod, Deployment), 사용권한(get, edit 등)을 매니페스트 파일에 명시해둔 규칙의 집합이 되며 클러스터 전체 사용 권한을 설정해줍니다.
- 롤은 특정 네임스페이스의 권한만을 주므로 롤과 클러스터롤은 차이점이 있습니다.
- 클러스터 롤 바인딩은 사용자와 클러스터를 묶어주는 역할을 수행하고, 지정한 사용자들에 한해서 롤에 명시한 규칙들을 기준으로 권한을 사용할 수 있도록 관리합니다.

### Role

- Kubernetes Cluster 는 Node, PV, Namespace 와 같이 공통되는 자원들이 있습니다.
- Cluster 의 Namespace 안에는 Pod, Svc
- Namespace 를 만들게 되면 ServiceAccount 가 자동으로 생성됩니다.
- Role은 여러개를 만들 수 있고, 각 Role 에는 네임스페이스 자원에 대해서 CRUD 에 대해 권한을 줄 수 있다.

### Rolebinding

- Role 과 ServiceAccount 를 연결해주는 역할을 한다.

### Cluster Access

- Namespace 내에서 Cluster 의 내용을 보고 싶다면 Cluster Role과 Cluster Rolebinding 을 설정해주어야 합니다.

### Role 사용법

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: role-01
  namespace: ns-01
rules:
- apiGroups: [""]
# apiGroups 는 k8s 내부 오브젝트면 지정하지 않아도 된다.
# - apiGroups:
#   - apiextensions.k8s.io
#   - apiextensions.k8s.io/v1beta1
#   resources:
#   - customresourcedefninitions
  verbs: ["get", "list"]
  resources: ["pods"]
```

### Rolebinding 사용법

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: rolebinding-01
  namespace: ns-01
roleRef:
  apiGroup: rbac.authorization.k8s.io/v1
  kind: Role
  name: role-01
subjects:
- kind: ServiceAccount
  name: default
  namespace: ns-01
```
