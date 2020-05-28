# OAuth 1.0과 2.0에 대해 알아보자

## OAuth 1.0

## 개념

**회사 사원이 건물에 출입하는 것이 로그인이라면
OAuth는 방문증을 수령한 후 회사에 출입하는 것에 비유할 수 있다.**

**방문증이란 사전에 정해진 곳만 다닐 수 있도록 하는 것이니, '방문증'을 가진 사람이 출입할 수 있는 곳과 '사원증'을 가진 사람이 출입할 수 있는 곳은 다르다.**

<li> 인증(Authentication): 인증과 허가의 차이는 명확하다. 간단하게 설명하면 인증은 우리가 평소에 어떠한 서비스를 이용하기 위해 '로그인을 하는 것' 이라고 생각하면 쉽다.
</li>
<li> 허가(Authorization): 인증 후 이용하고자하는 서비스안에서 어떠한 기능을 이용할 수 있는 권한을 허가 한다고 생각하면 된다. </li>

<h2> OAuth 1.0의 특징 </h2>
<p>기본의 다른 인증방식(OpenID) 과 구분되는 특징은 크게 두 가지이다.

1. API 인증 시, 써드파티 어플리케이션에게 사용자의 비번을 노출하지 않고 인증할 수 있다는 점
2. 인증(Authentication)과 API 권한(Authorization) 부여를 동시에 할 수 있다는 점</p>

<h2> OAuth 1.0의 동작방식 </h2>
<p>기본적으로 user / consumer / service provider가 있어야 한다. 부연설명 하기전에 간단하게 정의를하고 넘어가겠습니다. 우버라는 회사를 운영하고 있고, user는 우버라는 서비스에 네이버 로그인을 하려는 상황입니다.

user는 우버를 이용하기 위해 로그인을 수행해야 합니다. 따로 회원가입하기는 귀찮고, 소셜로그인 기능이 있어 네이버로그인 버튼을 클릭하였습니다.

1. user -> 우버 (네이버 로그인 요청)
2. 우버 -> 네이버 (사용자를 네이버 로그인 화면으로 **리다이렉트**)
3. 네이버 로그인 진행
4. 네이버 로그인 완료, 우버에게 인증토큰 전달

네이버는 우버에게 인증토큰(Access token)만을 전달하고 서비스에서 인증 토큰으로 네이버 API(Service Provider)를 사용할 수 있도록 해준다.

<h2>인증토큰의 장점 </h2>

* 사용자의 아이디/ 패스워드를 몰라도 토큰을 통해 허가 받은 API에 접근이 가능하다.
* 필요한 API에만 제한적으로 접근할 수 있도록 권한 제어 가능
* 저장되어 있는 인증토큰이 유출되더라도 네이버의 관리자 화면에서 인증토큰의 권한 취소 가능
* 사용자가 네이버(Service Provider)의 패스워드를 변경해도 인증토큰은 계속 유효
</p>

# OAuth 2.0
## 개념
OAuth 2.0은 1.0과 호환되지 않으며 용어부터 많은 것이 다르다.
모바일에서의 사용성 문제나 서명과 같은 개발이 복잡하고 기능과 규모의 확장성 등을 지원하기 위해 만들어진 표준이다. 표준이 매우 크고 복잡해서 이름도 "OAuth 인증 프레임워크" 이다.

## 개선된 점
1. 용어 변경
	* Resource Owner: 사용자
	* Resource Server: REST API 서버
	* Authorization Server: 인증서버 (API 서버와 같을 수도 있음)
	* Client: 써드파티 어플리케이션(서비스)
2. 간단하고 직관적
	* OAUth 1.0에서는 HTTPS가 필수
	* Signature 없이 생성, 호출 가능
	* URL 인코딩이 필요없음
3. 더 많은 인증방법을 지원
	* 이전에는 HMAC을 이용한 암호화 인증만 지원
	* OAuth 2.0은 여러 인증 방식을 통해 웹/모바일 등 다양한 시나리오에 대응 가능
	* Access Token의 Life-time을 지정하여 만료일 설정 가능
4. 대형 서비스로의 확장성 지원
	* 커다란 서비스는 인증 서버를 분리하거나 다중화 할 수 있어야 함
	* Authorization Server의 역할을 명확히 하여 이에 대한 고려가 되었음


## 용어정리
* Client (Application)
* Resource Owner (User)
* Resource Server (Provider)
* Client_id, Resource Server에서 Application을 생성할 때 발급됩니다.
* Client_secret, ID의 PW 노출되지 않게 주의하여야 합니다.
* redirect_uri: 서비스 제공자가 인가 요청에 대한 응답을 전달할 리다이렉션 엔드포인트
* scope: 요청하는 접근 범위
* state: 사용하는 것을 권장, 클라이언트의 요청과 그에 따른 콜백 간의 상태를 유지하기 위해 사용되며, 클라이언트가 서비스 제공자에게 전달하면 서비스 제공자는 이 값을 다시 응답에 포함해서 전달한다. CSRF 공격을 차단하기 위한 수단이 될 수 있다. 
추가로 설명하자면 클라이언트가 요청할 때 앱 고유 ID를 state에 넣어 요청했다고 가정하겠습니다. 서비스 제공자는 이 값을 받고 처리하고 응답할 때 state의 값을 다시 넘겨줍니다.  

## 사전 개념/준비

`Client` 에서 `Resource Server` 를 이용하려면 등록을 해야 됩니다.
* Client ID: Application을 식별하는 식별자
* Client Secret: Password
* Authorized redirect URLs: https://client/callback 
	* `Resource Server` 에서 Authorized Code를 전달해주는데 받을 URL을 지정해줍니다.

`Client(Application)`는 `Resource Owner(사용자)` 를 대신해 로그인하는데, 이 때 필요한 정보를 `Resource Server(Kakao)` 에서 얻어 서로 비교해 유효성을 판단합니다.

기존에 유저가 자신의 ID와 PW를 입력해 로그인하는 방법이아니라,
`Client`가 유저의 로그인 정보/자원(Resource)을 `Resource Server`에 요청해 대신 로그인 합니다.

이를 위해서는 `Client`는 다음 단계를 수행합니다.
1. `Resource Owner`로 부터 동의 ex) 소셜로그인 시 **앱에 Email, 생년월일 정보를 제공하는 것을 동의합니까?
2. `Resource Server`로 부터 `Client` 계정 확인 ex) `Client`의 계정이 `Resource Server`에 존재하는지?
3. `Authorization code`를 `Resource Server`는 `Resource Owner`에게 전송합니다.
ex) Location: https://client/callback?code=3 # 임시 비밀번호를 의미합니다.
4. `Resource Owner`는 `Client`으로 요청을 보내게되고, `Client`는 `Authorization code`를 얻게 됩니다.
ex) https://client/callback?code=3
5. `Resource Owner`를 통하지않고, `Resource Server`로 바로 요청을 합니다.
ex)  https://resource.server/token?grant_type=authorization_code&code=3&redirect_rui=https://client/callback&client_id=1&client_secret=2
6. `Client`가 요청한 `Authorization code`와 `Resource Server` 안에 있는 `Authorization code`를 비교합니다. 또 `Client_id`와 `Client_Secret`, `redirect_url`이 모두 일치한다면 다음 단계로 진행하게 됩니다.
7. 인증이 된 사용자이기 때문에 Authorization code를 없애줍니다.
8. Resource Server 는 Access Token을 Client에게 발급해줍니다. Client는 Access Token의 토큰 값을 저장하게 됩니다. Client는 발급 받은 Access Token을 가지고 Resource Server에 요청을 하게 되면 Resource Server는 내부에 해당하는 Access Token을 갖고 있는 정보를 찾아 그 정보가 허용하고 있는 권한을 열어주게 된다.




## Flow (Google)
1. 유저가 로그인 페이지에 접속을 한다.
2. 로그인 페이지 접속 시 유저를 식별하기 위해 생성한 랜덤한 `state` 값을 사용해 구글 로그인 링크를 생성한다.
3. 유저는 반환된 구글 로그인 링크를 클릭해 소셜 로그인을 진행한다.
4. 소셜 로그인 후에 구글 인증 서버는 토큰 발급을 위한 임시 `code` 값과 이전에 전송했던 `state` 값을 미리 등록했던 콜백 URL에 붙여 리다이렉트 한다.
5. 콜백 URL로 호출되는 인증 처리 핸들러에서는 `state` 값이 이전값과 같은지 확인한 뒤, 받은 `code` 값을 사용해 실제 리소스 사용 권한이 담긴 엑세스 토큰을 발급 받기 위해 구글 인증 서버로 요청을 보낸다.
6. 인증 서버로부터 엑세스 토큰을 받으면 필요한 리소스를 요청할 수 있게 된다.



# Reference
* [https://swalloow.github.io/about-oauth2](https://swalloow.github.io/about-oauth2)
* [https://kimdoky.github.io/oauth/2019/05/01/oauth-serverside-flow/](https://kimdoky.github.io/oauth/2019/05/01/oauth-serverside-flow/)
* [https://opentutorials.org/course/3405](https://opentutorials.org/course/3405)

<!--stackedit_data:
eyJoaXN0b3J5IjpbMjc0MDgwMTA1XX0=
-->