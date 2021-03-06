## 서브넷

- IP 를 사용하는 네트워크 장치들의 수에 따라 효율적으로 사용할 수 있는 것을 서브넷이라고 한다.

## 서브넷 마스크

- 서브넷 마스크는 IP 주소 체계의 Network ID 와 Host ID를 서브넷 마스크를 통해 변경하여서 '네트워크 영역을 분리 또는 합체' 시키는 개념이다.
- IP 주소에는 반드시 서브넷 마스크가 있다.
- 서브넷 마스크는 기본적으로 255와 0으로 이루어져 있다.
- 여기서 255는 네트워크 부분이며 0은 호스트 부분이 된다.
- 255로 된 부분은 무시하시고, 0으로 된 부분에서 IP 를 나눠쓰는 혹은 IP를 쪼개는 개념이다.
- 네트워크 수는 2의 제곱의 수로 계산하면된다.

## 서브네팅

- **서브넷팅은 서브넷 마스크를 이용하여 Host ID 를 Network ID 로 변환하게 됩니다.**

## Network ID, Host Id

- A 클래스의 경우 첫 번째 옥텟이 Network ID 이고 뒤에 세 개의 옥텟이 Host ID 이런 수순으로 나아간다.
- 라우터는 라우팅 할 때 Network ID 부분을 보고 (우편번호로 우체국이 동네를 찾듯이) 특정 컴퓨터의 위치를 빠르게 좁힌다. 그리고 목적지 네트워크에 도착하면 그 때 Host ID 를 보고 그 패킷을 특정 컴퓨터로 보낸다.
- 표기법은 IP 주소에서 네트워크 ID에 사용되는 비트 수를 /16, /24 와 같이 지정한다. 서브넷 마스크의 비트수를 의무한다.
