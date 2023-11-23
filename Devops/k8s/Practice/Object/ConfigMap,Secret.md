# ConfigMap, Secret

* 환경에 따라 변하는 값들은 외부에서 변경할 수 있다.
* 애플리케이션을 배포하다 보면, 환경에 따라서 다른 설정값을 사용하는 경우가 있다. 예를 들어, 데이타베이스의 IP, API를 호출하기 위한 API KEY, 개발//운영에 따른 디버그 모드, 환경 설정 파일들이 있는데, 애플리케이션 이미지는 같지만, 이런 환경 변수가 차이가 나는 경우 매번 다른 컨테이너 이미지를 만드는 것은 관리상 불편할 수 밖에 없다.
* 이러한 기능을 제공하는 것이 바로 ConfigMap 과 Secret 이다.
* **컨테이너 환경변수**에 ConfigMap과 Secret 값이 저장된다.
* ConfigMap과 Secret에 정의해놓고, 이 값을 Pod로 넘기는 방법은 크게 두 가지가 있다.
  * Pod의 **환경변수(Environment Variable)**로 넘기는 방법
  * Pod의 **디스크 볼륨으로 마운트** 하는 방법

## ConfigMap

* 설정 정보를 저장해놓는 일종의 저장소 역할
* Key, Value 를 무한히 넣을 수 있다.
* **literal(문자)**로 생성하는 방법과 **파일**로 생성하는 방법이 있다.

### literal

* kubectl create configmap [configmap 이름] --from-literal=[키]=[값] 식으로 생성 -> kubectl create configmap hello-tim --from-literal=language=python

아래와 같이 yaml 파일로도 ConfigMap 을 생성할 수 있다.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: hello-tim
data:
  language: python

# Deployment 정의
apiVersion: apps/v1beta2
kind: Deployment
metadata:
  name: cm-deployment
 spec:
   replicas: 3
    minReadySeconds: 5
     selector:
        matchLabels:
           app: cm-literal
        template:
           metadata:
              name: cm-literal-pod
               labels:
                  app: cm-literal
               spec:
                  containers:
                   - name: cm
                      image: gcr.io/terrycho-sandbox/cm:v1        imagePullPolicy: Always
                       ports:
                        - containerPort: 8080
                         env:  # 환경변수 정의
                          - name: LANGUAGE
                             valueFrom:  # 데이터는 valueFrom 을 이용해서 configMap 을 읽어오도록 하였다.
                                configMapKeyRef:
                                    name: hello-tim
                                    key: language
```

## Secret

* 1MB 용량으로 제한되어 있다.

# Reference

* https://bcho.tistory.com/1267