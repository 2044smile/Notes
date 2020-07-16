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

### 생성 된 ArgoWorkflow 를 사용 submit
```yaml
apiVersion: argoproj.io/v1alpha1
kind: Sensor
metadata:
  name: webhook
spec:
  template:
    serviceAccountName: argo-events-sa
  dependencies:
    - name: test-dep
      gatewayName: webhook
      eventName: example
  subscription:
    http:
      port: 9300
  triggers:
    - template:
        name: argo-workflow-trigger
        argoWorkflow:
          group: argoproj.io
          version: v1alpha1
          resource: workflows
          operation: submit
          source:
            resource:
              apiVersion: argoproj.io/v1alpha1
              kind: Workflow
              metadata:
                name: special-trigger
              spec:
                entrypoint: whalesay
                arguments:
                  parameters:
                    - name: message
                      # the value will get overridden by event payload from test-dep
                      value: hello world
                templates:
                  - name: whalesay
                    serviceAccountName: argo-events-sa
                    inputs:
                      parameters:
                        - name: message
                    container:
                      image: docker/whalesay:latest
                      command: [cowsay]
                      args: ["{{inputs.parameters.message}}"]
          parameters:
            - src:
                dependencyName: test-dep
              dest: spec.arguments.parameters.0.value
```


### 여러개의 webhook 을 한 sensor에서 실행
```yaml
apiVersion: argoproj.io/v1alpha1
kind: Sensor
metadata:
  name: circuit-sensor
spec:
  template:
    serviceAccountName: argo-events-sa
  dependencies:
    - name: test-dep-webhook
      gatewayName: webhook-gateway
      eventName: example
    - name: test-dep-minio
      gatewayName: minio-gateway
      eventName: example

  # group event dependencies
  dependencyGroups:
    - name: group_1
      dependencies:
        - test-dep-webhook
    - name: group_2
      dependencies:
        - test-dep-minio

  # trigger when either group_1 or group_2 resolves
  circuit: "group_1 || group_2"

  subscription:
    http:
      port: 9300
  triggers:
    - template:
        # when is the switch that determines whether to execute the trigger or not
        switch:
          # all is boolean equivalent of AND.
          # you can use `any` as well which is boolean equivalent of OR.
          all:
            - group_1
        name: workflow-trigger-1
        k8s:
          group: argoproj.io
          version: v1alpha1
          resource: workflows
          operation: create
          source:
            resource:
              apiVersion: argoproj.io/v1alpha1
              kind: Workflow
              metadata:
                generateName: group-1-
              spec:
                serviceAccountName: argo-events-sa
                entrypoint: whalesay
                templates:
                  - name: whalesay
                    container:
                      args:
                        - "hello world"
                      command:
                        - cowsay
                      image: "docker/whalesay:latest"
          parameters:
            - src:
                dependencyName: test-dep-webhook
                dataKey: body.message
              dest: spec.templates.0.container.args.0
    - template:
        switch:
          all:
            - group_2
        name: workflow-trigger-2
        k8s:
          group: argoproj.io
          version: v1alpha1
          resource: workflows
          operation: create
          source:
            resource:
              apiVersion: argoproj.io/v1alpha1
              kind: Workflow
              metadata:
                generateName: group-2-
              spec:
                serviceAccountName: argo-events-sa
                entrypoint: whalesay
                templates:
                  - name: whalesay
                    container:
                      args:
                        - "hello world"
                      command:
                        - cowsay
                      image: "docker/whalesay:latest"
          parameters:
            - src:
                dependencyName: test-dep-minio
                dataKey: s3.bucket.name
              dest: spec.templates.0.container.args.0
```


### Webhook 트리거 병렬
```yaml
apiVersion: argoproj.io/v1alpha1
kind: Sensor
metadata:
  name: webhook
spec:
  template:
    serviceAccountName: argo-events-sa
  subscription:
    http:
      port: 9300
  dependencies:
    - name: test-dependency
      gatewayName: webhook
      eventName: example
  triggers:
    - template:
        name: multi-trigger-workflow-1
        k8s:
          group: argoproj.io
          version: v1alpha1
          resource: workflows
          operation: create
          source:
            s3:
              bucket:
                name: workflows
                key: hello-world.yaml
              endpoint: minio-service.argo-events:9000
              insecure: true
              accessKey:
                key: accesskey
                name: artifacts-minio
              secretKey:
                key: secretkey
                name: artifacts-minio
    - template:
        name: multi-trigger-workflow-2
        k8s:
          group: argoproj.io
          version: v1alpha1
          resource: workflows
          operation: create
          source:
            resource:
              apiVersion: argoproj.io/v1alpha1
              kind: Workflow
              metadata:
                generateName: hello-world-
              spec:
                entrypoint: whalesay
                templates:
                  -
                    container:
                      args:
                        - "hello world"
                      command:
                        - cowsay
                      image: docker/whalesay:latest
                    name: whalesay
```



### Reference 

https://argoproj.github.io/argo-events/installation/