### ENTRYPOINT 와 CMD 는 무엇인가
- ENTRYPOINT 와 CMD는 해당 컨테이너가 수행하게 될 실행 명령을 정의하는 선언문이다.
 즉, 컨테이너가 무슨 일을 하는지 결정하는 최종 단계를 정의하는 명령이라고 생각하면 된다. 그렇기 때문에 가장 마지막 부분 쯤에 ENTRYPOINT 또는 CMD를 선언하게 된다.
 
### 차이점
- 가장 큰 차이점은 컨테이너 시작 시 실행 명령어 대한 Default 지정 여부이다.
- 만약 ENTRYPOINT를 사용하여 컨테이너 수행 명령을 정의한 경우, 해당 컨테이너가 수행될 때 반드시 ENTRYPOINT 에서 지정한 명령을 수행되도록 지정된다.
- 하지만 CMD를 사용하여 수행 명령을 줄 경우에는 컨테이너를 실행할 때 인자 값을 주게 되면 Dockerfile 에 지정 된 CMD 값을 대신하여 지정한 인자값으로 변경하여 실행되게 된다.

### CMD 예시를 살펴보도록 하자.
```dockerfile
FROM ubuntu
CMD ["/bin/df", "-h"] # CMD 의 경우 생성 시에 -h 옵션이라는 인자값을 지정해주었다.
```

생성한 이미지를 컨테이너로 동작시켜보면
```dockerfile
> docker run --name jhsong-df jhsong/df
```

/bin/df -h 옵션의 결과가 나온다.
CMD 는 컨테이너를 실행할 때 추가 인자 값을 줘서 컨테이너가 수행할 명령어를 변경할 수 있다.
```dockerfile
> docker run --name jhsong-df jhsong/df ps -aef
```

### ENTRYPOINT 예시를 살펴보도록 하자
CMD 예시와 똑같은 파일을 생성하였습니다.
```dockerfile
FROM ubuntu 
ENTRYPOINT ["/bin/df", "-h"]

> docker run --name jhsong-df jhsong/df:entry ps -aef

# 에러발생
# /bin/df: invalid option -- 'e' 
# Try '/bin/df --help' for more information.
```
- ENTRYPOINT 의 경우 컨테이너 실행 시 /bin/df 명령은 유지하고, 추가 인자를 CMD로 받아 처리합니다.
- 결국 컨테이너 시작 시 아래와 같은 명령어를 수행한 것 입니다.
```
df -h ps -aef
```
- 정리해보면 ENTRYPOINT 로 생성한 도커 이미지를 실행 시 인자값을 주게 되면 CMD 에 입력한 것 처럼 앞에 이동한다는 것 입니다.
- 우리는 ps -aef 라는 옵션을 주려고 했는데 이것이 "ps -aef df -h" 를 만들어낸 것 이죠.

### 올바른 사용방법
1. 컨테이너가 수행될 때 변경되지 않을 실행 명령은 CMD 보다는 ENTRYPOINT로 정의하는게 좋다.
2. 메인 명령어 실행 시 default option 인자 값은 CMD 로 정의하는 것이 좋다.
3. ENTRYPOINT 와 CMD 를 작성할 때는 리스트 포맷 (["args1", "args2", . . .]) 으로 정의해주는 것이 좋다.


### Reference
- https://bluese05.tistory.com/77