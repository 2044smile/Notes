# Argo Workflow Events

### Events Installation
- Create The namespace

```
kubectl create namespace argo-events
```

- Deploy Argo Events, SA, ClusterRoles, ConfigMap, Sensor Controller and Gateway Controller

```
kubectl apply -f https://raw.githubusercontent.com/argoproj/argo-events/stable/manifests/install.yaml
```

- Namespace installation

```
kubectl apply -f https://raw.githubusercontent.com/argoproj/argo-events/stable/manifests/namespace-install.yaml
```

### Parameterization
- 파라미터화를 시킴으로써 입력 된 파라메타로 원하는 동작을 할 수 있음

### Trigger Sources


### Webhook Setup
- Setup

```
kubectl apply -n argo-events -f https://raw.githubusercontent.com/argoproj/argo-events/stable/examples/gateways/webhook.yaml
```

### 내가 쓰려고 정리한 튜토리얼 생성
```yaml
kubectl create namespace argo-events

kubectl apply -f https://raw.githubusercontent.com/argoproj/argo-events/stable/manifests/install.yaml
```



### Reference 

https://argoproj.github.io/argo-events/installation/