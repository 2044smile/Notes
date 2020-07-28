### Argo Workflow


### Argo input & output
- 디렉토리나 파일을 다음 단계로 전달하기 위해서는 사용해야하는 몇 가지 시나리오가 있습니다.
1. 매개 변수(parameters)를 사용하는 방법
- 매개 변수 방법은 특정 텍스트의 내용을 읽고 다음 단계로 전달하는 것 입니다.
#### EXAMPLE(https://github.com/argoproj/argo/blob/master/examples/output-parameter.yaml)


2. 아티팩트(artifacts)를 사용하는 방법


### 스크립트를 돌리고 파일을 생성하는 로직
```yaml
apiVersion: argoproj.io/v1alpha1
kind: WorkflowTemplate
metadata:
  name: init-
spec:
  entrypoint: start-workflow
  templates:
  - name: start-workflow
    steps:
    - - name: get-uuid  # GET UUID
        template: create-uuid

  - name: create-uuid
  container:
    image: python:alpine3.6
    command: ["bin/sh"]
    args: ["-c", "python -c \"import uuid; print(uuid.uuid4())\" > /tmp/uuid.txt"]
    # bin/sh 로 들어가서 실행해야 한다 > /tmp/uuid.txt 는 shell 명령어 이기 때문에
  outputs:
    parameters:
    - name: global-uuid
      valueFrom:
        path: /tmp/uuid.txt
      globalName: global-uuid
```


#### global parameter
- 글로벌 파라메타라는데 다른 yaml(workflow) 에서도 사용할 수 있을까?
```yaml
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: global-parameters-
spec:
  entrypoint: A
  arguments:
    parameters:
    - name: log-level
      value: INFO

  templates:
  - name: A
    container:
      image: containerA
      env:
      - name: LOG_LEVEL
        value: "{{workflow.parameters.log-level}}"
      command: [runA]
  - name: B
    container:
      image: containerB
      env:
      - name: LOG_LEVEL
        value: "{{workflow.parameters.log-level}}"
      command: [runB]
```

#### single dash, double dash
- double dash => run after previous step
- single dash => run in parallel with previous step
```yaml
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: steps-
spec:
  entrypoint: hello-hello-hello

  # This spec contains two templates: hello-hello-hello and whalesay
  templates:
  - name: hello-hello-hello
    # Instead of just running a container
    # This template has a sequence of steps
    steps:
    - - name: hello1            # hello1 is run before the following steps
        template: whalesay
        arguments:
          parameters:
          - name: message
            value: "hello1"
    - - name: hello2a           # double dash => run after previous step
        template: whalesay
        arguments:
          parameters:
          - name: message
            value: "hello2a"
      - name: hello2b           # single dash => run in parallel with previous step
        template: whalesay
        arguments:
          parameters:
          - name: message
            value: "hello2b"

  # This is the same template as from the previous example
  - name: whalesay
    inputs:
      parameters:
      - name: message
    container:
      image: docker/whalesay
      command: [cowsay]
      args: ["{{inputs.parameters.message}}"]
```
### Scripts & Results
- 간단한 스크립트는 아래와 같이 작성할 수 있음

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: scripts-bash-
spec:
  entrypoint: bash-script-example
  templates:
  - name: bash-script-example
    steps:
    - - name: generate
        template: gen-random-int-bash
    - - name: print  # 가장 중요한 부분
        template: print-message
        arguments:
          parameters:
          - name: message
            value: "{{steps.generate.outputs.result}}"  # The result of the here-script / generate의 실행결과를 가져와서 message 로 넘길 수 있음

  - name: gen-random-int-bash
    script:
      image: debian:9.4
      command: [bash]
      source: |                                         # Contents of the here-script
        cat /dev/urandom | od -N2 -An -i | awk -v f=1 -v r=100 '{printf "%i\n", f + r * $1 / 65536}'

  - name: gen-random-int-python
    script:
      image: python:alpine3.6
      command: [python]
      source: |
        import random
        i = random.randint(1, 100)
        print(i)

  - name: gen-random-int-javascript
    script:
      image: node:9.1-alpine
      command: [node]
      source: |
        var rand = Math.floor(Math.random() * 100);
        console.log(rand);

  - name: print-message
    inputs:
      parameters:
      - name: message
    container:
      image: alpine:latest
      command: [sh, -c]
      args: ["echo result was: {{inputs.parameters.message}}"]
```

### WorkflowTemplate Ref
- 한 개의 워크플로우 템플릿에 정의한 여러 워크플로우를 가져올 때는 이름만 명시해주면 손쉽게 가져올 수 있습니다.

```yaml
apiVersion: argoproj.io/v1alpha1
kind: WorkflowTemplate
metadata:
  name: hello
spec:
  entrypoint: start-workflow
  templates:
  - name: start-workflow
    steps:
    - - name: getuuid  # 직접 명시하는 식으로 가져올 수도 있고,
        template: uuid
    - - name: ref
        templateRef:
          name: # 명시 할 WorkflowTemplate name 
          template: # 명시 할 template name

  - name: uuid
    script:
      image: python:alpine3.6
      command: [python]
      source: |
        import uuid
        print(uuid.uuid4())
```

### Reference
- https://argoproj.github.io/argo/