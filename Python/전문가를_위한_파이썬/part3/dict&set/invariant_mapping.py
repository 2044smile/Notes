# 3.7 불변 매핑
## 표준 라이브러리에서 제공하는 매핑형은 모두 가변형이지만, `사용자가 실수로 매핑을 변경하지 못하도록 보장하고 싶은 경우가 있을 것이다.`
## 하드웨어를 소프트웨어로 변경할 수 없기 때문에 물리적인 디바이스 특성을 반영해서 사용자가 실수로 board.pins를 변경하지 못하도록 막는 것이 좋다.

### 3-9. `dict 에서 읽기 전용` mappingproxy 객체를 생성하는 MappingProxyType
from types import MappingProxyType


d = {1: 'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)  # mappingproxy({1: 'A'})

d_proxy[2] = "start"  # TypeError: 'mappingproxy' object does not support item assignment 
# 즉 d_proxy 는 변경할 수 없다. 

d[2] = "finish"
print(d_proxy)  # mappingproxy({1: 'A', 2: 'finish'})
print(d_proxy[2])  # finish

## mappingproxy로 구현한 pins 속성을 공개해서 API 사용자에게 제공함으로써 불변형 매핑을 사용할 수도 있다.
## 이렇게 하면 클라이언트가 실수로 핀을 추가, 삭제, 변경할 수 없게 된다.
