# Apple Social Login

## 개요

- Apple은 사용자가 Apple ID를 사용하여 앱에 로그인 할 수 있는 새로운 기능인 "Apple로 로그인"을 발표했습니다. 이 새로운 기능은 사용자가 앱에서 계정을 생성할 수 있는 안전하고 개인 정보 보호를 위한 방법입니다. 대부분의 iOS 및 Mac 사용자는 이미 Apple ID 를 가지고 있으며 새로운 기능을 통해 해당 Apple ID 를 사용하여 다른 앱과 웹 사이트에 로그인할 수 있습니다.

## 이메일 보안

- 애플은 애플리케이션이 사용자의 실제 이메일 주소를 볼 수 있도록 하는 것이 아니라 사용자의 개인 정보를 보호하기 위해 확고한 입장을 취하고 있으며 각 앱에 고유 한 가짜 또는 임의의 이메일 주소를 앱에 제공할 것 입니다. ex) applemaster@privacyapple.com 이런식으로 생성됩니다.

## 작동 원리

- Apple 은 새로운 API의 기반으로 사용하기 위해 기존 표준 OAuth 2.0 및 OpenID Connect를 채택했습니다.

## 1. 키 생성

- 필요한 키를 생성합니다.
  - key_id
  - team_id
  - client_id
  - client_secret
  - redirect_uri
- 처음 세 개의 키는 Apple Dev 계정에서 가져올 수 있습니다.

```pip install pyjwt```

```python
import jwt

headers = {
    'kid': settings.SOCIAL_AUTH_APPLE_KEY_ID
}
payload = {
    'iss': settings.SOCIAL_AUTH_APPLE_TEAM_ID,
    'iat': timezone.now(),
    'exp': timezone.now() + timedelta(days=180),  # Apple Dev 에서 제공해주는 Secret 키는 6개월이 지나면 만료됩니다.
    'aud': 'https://appleid.apple.com',
    'sub': settings.CLIENT_ID,  # Apple Dev 에서 가져올 수 있습니다.
}
client_secret = jwt.encode(
    payload,
    settings.SOCIAL_AUTH_APPLE_PRIVATE_KEY,
    algorithm='ES256',  # 암호화(encode) 할 알고리즘을 결정합니다.
    headers=headers
)
```

- Application 에서 Apple Login 버튼 생성
  - redirect_uri: 사용자가 Apple Login 화면에서 로그인하여 인증하고, 인증이 성공하면 redirect_uri 로 서비스에 필요한 정보를 넘겨줍니다.
  - clientId: Apple Develop 사이트에서 생성한 clientId를 입력합니다.
  - scope: 사용자의 정보를 가져올 수 있습니다. ex) scope: 'name email'
  - state: 클라이언트의 요청과 그에 따른 콜백 간의 상태를 유지하기 위해서 사용됩니다.

## Application

- 애플리케이션에서는 클라이언트가 클릭할 수 있는 버튼을 아래와 같이 생성해주고, Apple 에서 제공받을 버튼을 생성해줍니다

```html
<html>
    <head>
    </head>
    <body>
        <script type="text/javascript" src="https://appleid.cdn-apple.com/appleauth/static/jsapi/appleid/1/en_US/appleid.auth.js"></script>
        <div id="appleid-signin" data-color="black" data-border="true" data-type="sign in"></div>
        <script type="text/javascript">
            AppleID.auth.init({
                clientId : '<Apple Develop 에서 생성한 Id>',
                scope : 'email',
                redirectURI: '<redirect_uri>',
                state : 'initial',
            });
        </script>
    </body>
</html>

```

## 2. Backend 구현

- Python 소셜 인증은 OAuth 2.0 표준이지만 Apple은 흐름에 약간의 차이가 있습니다. 따라서 Apple 로그인을 완료하려면 BaseOAuth2를 확장하고 일부 기능을 사용자가 정의하거나 재정의해야합니다.

### GET id_token

- 토큰 유효성 검사 호출에 대한 응답으로 Apple은 여러 가지가 포함 된 id_token을 반환하지만 두 가지가 중요합니다. Email 및 Sub 여기서 sub는 고유한 user_id이고 email은 가짜 또는 실제 사용자의 이메일 ID 입니다.
(여기서 가짜 또는 실제 사용자의 이메일이라는 것은 사용자가 이메일 공개를 꺼려하여 설정을 하였다면 도메인 부분이 가짜 도메인으로 변경됩니다.)

```python
decoded = jwt.decode(id_token, '', verify=False)
```

- id_token 을 받아오기 위해선 ACCESS_TOKEN_URL 이 필요합니다.
ex) POST 'https://appleid.apple.com/auth/token'
- 같이 보낼 데이터는
  - client_id  # APple Dev
  - client_secret  # Apple Dev
  - code  # Front 에서 설정한 redirect_uri 에서 받아올 수 있습니다.
  - grant_type
  - redirect_uri

```python
response_data = {}
client_id, client_secret = self.get_key_and_secret()

headers = {'content-type': "application/x-www-form-urlencoded"}
data = {
    'client_id': client_id,
    'client_secret': client_secret,
    'code': access_token,
    'grant_type': 'authorization_code',
    'redirect_uri': 'https://example-app.com/redirect'
}

res = requests.post(AppleOAuth2.ACCESS_TOKEN_URL, data=data, headers=headers)

# ACCESS_TOKEN_URL 에는 /auth/token 으로 요청하는 URL이 들어있습니다.

response_dict = res.json()
```

## Response

- 여기서 한가지 알아야할 것은 사용자 이메일과 이름은 처음 요청할 때만 반환된다는 것 입니다.

## Reference

[sign-in-with-apple](https://gist.github.com/aamishbaloch/2f0e5d94055e1c29c0585d2f79a8634e)