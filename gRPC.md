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
	* 클라우드 서버와 커뮤니케이션하는 모바일 클라이언트를 지원하는데 초점이 맞춰져 있습니다.
* **HTTP/2를 이용한 reverse proxy 기능**
	* 서버간에 HTTP 1.1 Keep-alive로 통신하고 있을 경우, 특정 요청이 holding 되면 다음 요청도 전부 holding되는 문제가 생길 수 있습니다.
	* HTTP/2 reverse proxy를 통해 multiplex하게 서버와 요청을 주고 받을 수 있게 됩니다.
		* ex) 여러 모듈들을 multiplex 하게 트리거할 수 있음(?) 
* **Protocol Buffer**
	* XML, json 등으로 들어온 요청 / 응답을 Protocol Buffer를 이용해 직렬화하여 더 작은 크기의 요청 / 응답으로 만들 수 있습니다.
	* 기본적으로는 base128을 이요한 byte array 직렬화를 사용하지만, 사용방식에 따라 json, text 직렬화로 사용 가능합니다.
		* ex) helloworld.proto 아래와 같이 스크립트를 만들어두고 python 의 경우 
		`python -m grpc_tools.protoc -I. --python_out=.--grpc_python_out=. helloworld.proto` 명령을 입력하면 
		``` 
		syntax = "proto3";
		package helloworld;
		
		service Greeter {
		  rpc SayHello (HelloRequest) returns (HelloReply) {}
		}

		message HelloRequest {
		  string name = 1;
		}

		message HelloReply {
		  string message = 1;
		}
		 ```

## Reference 
* [https://widian.github.io/blog/2018/11/23/grdc-%EC%A0%95%EB%A6%AC.html](https://widian.github.io/blog/2018/11/23/grdc-%EC%A0%95%EB%A6%AC.html)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwODk4Mzg5ODFdfQ==
-->