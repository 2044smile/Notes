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

- Backend 에서 

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