<h2 id="grpc란">gRPC란</h2>
<ul>
<li>gRPC는 어떤 환경에서도 동작하는 모던한 오픈소스 원격 프로시저 요청 (Remote Procedure Call, RPC) 프레임워크입니다.</li>
<li>gRPC는 구글에서 10년 이상동안 수 많은 MSA와 데이터센터 사이를 연결하기 위해 사용하던 Stubby라고 부르던 범용 RPC 인프라를 크로스플랫폼, 오픈소스화해서 만들어졌습니다.</li>
<li>gRPC stub
<ul>
<li>client side에서 요청을 gRPC 형태로 만들어주는 역할을 하는 컴포넌트의 이름입니다.<br>
ex) <code>stub = helloworld_pb2_grpc.GreeterStub(channel)</code></li>
</ul>
<li>proto buf를 이용하여 gRPC가 지원하는 언어에 안에서는 서로 통신이 가능하다.</li>
<li>HTML1.1 보다 2.0의 속도가 약 10배 이상 Amazing</li>
<li>gRPC를 사용하게 되면 Restful HTTP의 규격이 필요가 없다.</li>
<li>user_pb2.py -> Message 정의에 사용될 Class</li>
<li>user_pb2_grpc.py -> Service 정의에 사용될 Class</li>
</ul>
<h2 id="grpc가-반드시-제공해야할-기능">gRPC가 반드시 제공해야할 기능</h2>
<ul>
<li>Service not Objects, Messages not References</li>
<li>Streaming</li>
<li>Blocking &amp; Non-Blocking</li>
</ul>
<h2 id="장점">장점</h2>
<ul>
<li>Low Latency, Highly scalable, distributed systems
<ul>
<li>클라우드 서버와 커뮤니케이션하는 모바일 클라이언트를 지원하는데 초점이 맞춰져 있습니다.</li>
</ul>
</li>
<li><strong>HTTP/2를 이용한 reverse proxy 기능</strong>
<ul>
<li>서버간에 HTTP 1.1 Keep-alive로 통신하고 있을 경우, 특정 요청이 holding 되면 다음 요청도 전부 holding되는 문제가 생길 수 있습니다.</li>
<li>HTTP/2 reverse proxy를 통해 multiplex하게 서버와 요청을 주고 받을 수 있게 됩니다.
<ul>
<li>ex) 여러 모듈들을 multiplex 하게 트리거할 수 있음(?)</li>
</ul>
</li>
</ul>
</li>
<li><strong>Protocol Buffer</strong>
<ul>
<li>XML, json 등으로 들어온 요청 / 응답을 Protocol Buffer를 이용해 직렬화하여 더 작은 크기의 요청 / 응답으로 만들 수 있습니다.</li>
<li>기본적으로는 base128을 이요한 byte array 직렬화를 사용하지만, 사용방식에 따라 json, text 직렬화로 사용 가능합니다.
<ul>
<li>ex) helloworld.proto 아래와 같이 스크립트를 만들어두고 python 의 경우<br>
<code>python -m grpc_tools.protoc -I. --python_out=.--grpc_python_out=. helloworld.proto</code> 명령을 입력하면 <code>helloworld_pb2.py</code>와 <code>helloworld_pb2_grpc.py</code> 가 생성됩니다.</li>
</ul>
<pre><code>syntax = "proto3";
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
</code></pre>
</li>
</ul>
</li>
</ul>


<h2>단점</h2>
<ul>
<li>엔드포인트의 추가와 파일 관리가 어렵다.</li>
예를 들어 MSA로 구성된 서비스이고, 모든 엔드포인트를 하나의 gRPC에서 관리하고 있다.
공통으로 사용하는 엔드포인트의 수정이 발생하였고, proto 파일을 생성하였고, pb2, pb2_grpc가 생성된다.
생성 된 파일들을 모듈들에게 적용시켜줘야된다는 불편함이 생긴다.
<li>Reference 에 있는 youtube를 보면 막바지에 그 불편함을 개선한 방법을 설명하니 자세한 설명이 필요하면 참고하면 됩니다.</li>

</ul>

<h2 id="reference">Reference</h2>
<ul>
<li><a href="https://widian.github.io/blog/2018/11/23/grdc-%EC%A0%95%EB%A6%AC.html">https://widian.github.io/blog/2018/11/23/grdc-%EC%A0%95%EB%A6%AC.html</a></li>
<a href="">https://www.youtube.com/watch?v=KGAernd-42M</a>
</ul>

