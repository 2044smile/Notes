## gRPC란
* gRPC는 어떤 환경에서도 동작하는 모던한 오픈소스 원격 프로시저 요청 (Remote Procedure Call, RPC) 프레임워크입니다.
* gRPC는 구글에서 10년 이상동안 수 많은 MSA와 데이터센터 사이를 연결하기 위해 사용하던 Stubby라고 부르던 범용 RPC 인프라를 크로스플랫폼, 오픈소스화해서 만들어졌습니다.
* gRPC stub
	* client side에서 요청을 gRPC 형태로 만들어주는 역할을 하는 컴포넌트의 이름입니다.
	ex) `stub = helloworld_pb2_grpc.GreeterStub(channel)`

## gRPC가 반드시 제공해야할 기능
* Service not Objects, Messages not References
* Streaming
* Blocking & Non-Blocking

## 장점
* Low Latency, Highly scalable, distributed systems
	* 

## Reference 
* [https://widian.github.io/blog/2018/11/23/grdc-%EC%A0%95%EB%A6%AC.html](https://widian.github.io/blog/2018/11/23/grdc-%EC%A0%95%EB%A6%AC.html)
<!--stackedit_data:
eyJoaXN0b3J5IjpbODc5NTI5MTA3XX0=
-->