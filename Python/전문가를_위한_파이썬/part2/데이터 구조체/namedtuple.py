# 2.3.4 명명된 튜플
## collections.namedtuple() 함수는 필드명과 클래스명을 추가한 튜플의 서브클래스를 생성하는 팩토리 함수로서, 디버깅 할 때 유용하다.
import collections


Card = collections.namedtuple('Card', ['rank', 'suit'])
# 명명된 튜플(namedtuple) 을 정의해서 도시에 대한 정보를 담고 있는 객체를 만드는 방법을 보여준다.

## 예제 2-9 명명된 튜플형을 정의하고 사용하기
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
tokyo

# 예제 2-10
City._fields  # (name, countey, population, coordinates)
LatLong = namedtuple('LatLong', 'lat long')
delhi_date = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))  # delhi_date[3].lat, delhi_date[3].long
delhi = City._make(delhi_date)  # == City(*delhi_data)
print(delhi)  # City(name='Delhi NCR', country='IN', population=21.935, coordinates=LatLong(lat=28.613889, long=77.208889))

delhi._asdict()  # {'name': 'Delhi NCR', 'country': 'IN', 'population': 21.935, 'coordinates': LatLong(lat=28.613889, long=77.208889)}
for key, value in delhi._asdict().items():
    print(key + ':', value)  # key + ":" + value 가 안되는 이유는 value 가 정수형과 실수형이 존재
    # name: Delhi NCR
    # country: IN
    # population: 21.935
    # coordinates: LatLong(lat=28.613889, long=77.208889)
