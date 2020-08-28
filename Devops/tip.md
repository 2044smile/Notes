## TIP (k8s, Argo, Docker, AWS)

### Kubernetes 의 Pod 이 실행할 때 수행한 명령어를 볼 수 있습니다.
- ```k get describe <pod name>```
- Containers -> main -> command:
- ```k logs -f <podname>  -c gateway-client ```
- 띄워진 팟의 로그를 볼 수 있습니다. 뒤에 -c 는 떄에 따라 사용할 때가 있고 없을 때가 있습니다. 


### minikube 는 부팅 시에 자동으로 실행이 안된다.
- [ERROR] Unable to connect to the server: dial tcp i/o time out
- [stackoverflow] https://stackoverflow.com/questions/49260135/unable-to-connect-to-the-server-dial-tcp-i-o-time-out


### Argo 에서 실행한 Workflow(Pod) 들을 한번에 제거할 수 있습니다.
Ex) Parallel 하게 50개의 워크가 돌아간다고하면 삭제할 때 귀찮다.

```argo delete -—all```

이 명령어를 사용하려면 Argo cli 를 설치해야 합니다.

### Docker Volume

```-v $HOME/.aws:/root/.aws``` 

```docker run -it -v $HOME/.aws:/root/.aws docker-image/docker-register/image-name:test-0.0.1``` 

### Entrypoint 로 생성한 container 에 접속하는 법

```docker run -it --entrypoint=/bin/bash docker-image/docker-register/image-name:test-0.0.1``` 

### AWS Configure 가 많은 경우 특정 profile 을 사용하고 싶을 때 

```AWS_PROFILE=test python manage.py runserver```

### crd 파일은 CustomResourceDefinition의 줄임말이고 이것을 생성하고 싶을 때

- 내렸다가 올려야 합니다.

```helm delete <release name>```

```helm install <release name> . ```

### kubectl config set-context

- context 를 수정할 때 사용할 수 있습니다.

```kubectl config set-context <cluster_name> --namepsace=<namespace>```

- 현재 클러스터 내에서 네임스페이스만 변경하려면

```kubectl config set-context --current --namepsace=<namespace>```
