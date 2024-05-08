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

# 2.3.5 불변 리스트로서의 튜플
# https://benban.tistory.com/93#:~:text=%EB%B0%98%EB%B3%B5%EC%9E%90(iterator)%EB%A5%BC%20%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94%20%EC%9D%B4%EC%9C%A0&text=iterator%EB%A5%BC%20%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94%EB%8D%B0%20%EC%97%AC%EB%9F%AC,%EB%A5%BC%20%ED%95%99%EC%8A%B5%ED%95%9C%EB%8B%A4%EA%B3%A0%20%EA%B0%80%EC%A0%95%ED%95%B4%EB%B3%B4%EC%9E%90.
## 튜플을 불변 리스트로 사용할 때, 튜플과 리스트가 얼마나 비슷한지 알고 있으면 도움이 된다.
### 튜플은 항목을 추가하거나 삭제하는 기능 및 __reversed__() 메서드를 제외하고 리스트가 제공하는 메서드를 모두 지원한다.

# 리스트나 튜플에서 볼 수 있는 메서드
lst = []
lst.__add__([1])  # [1]
print(lst)  # []

lst.__iadd__([1, 2])
print(lst)  # [1, 2]

# append() 제일 뒤에 요소를 하나 추가
# clear() 청소
# __contains__(3) -> False
# __contains__(1) -> True
# copy() 리스트를 얇게 복사
llst = lst.copy()
id(llst)  # 333
id(lst)  # 111
id(llst[0])  # 999
id(lst[0])  # 999
# lst.count(1)  # 1

# ___delitem__()
lst.__delitem__(1)  # 인덱스를 입력 [1, 2] -> [1]
# extend(it) 반복형 it 안에 있는 요소를 추가한다.
lst.extend(llst)
# __getitem__(index) # s[p], p 위치(인덱스)의 요소를 가져온다.
lst.__getitem__(1)
# __getnewargs__() # pickle을 이용해서 최적화된 직렬화를 지원한다.
# lst.__getnewargs__()  Python3 에서는 지원하지 않음
# index()
lst.index(1)  # 0 -> [`1`, 1, 2]
# insert()
lst.insert(0, 99)  # insert(p, e) p 위치에 있는 요소 앞에 e 요소를 삽입한다.
# __iter__()
lst.__iter__()  # <list_iterator at ...>
# __len__() == len(lst)
# __mul__()
lst.__mul__(3)  # __mul__(n) n 은 반복 횟 수를 의미한다. lst * n 문자열을 반복한다.
# __imul__()  # lst = lst * n
lst.__imul__(3)  # 문자열을 반복하여 lst 에 저장한다.
# __rmul__()  # __rmul__(n) `역순 반복`` 추가 메서드
# pop([p])  마지막 항목이나 p 위치(인덱스)의 항목을 제거하고 반환한다.
lst.pop(0)  # 출력(반환) 99 -> [1, 1, 2]
# remove(e)  # e 값을 가진 `첫 번째 항목`을 삭제한다.
lst.remove(1)  # [1, 1, 2] -> [1, 2]
# reverse()  # 항목을 역순으로 배치한 후 s에 저장한다.
lst.reserse()  # [1, 2] -> [2, 1]
# __reversed__()  # 
# lst = [2, 1]
lst.__reversed__()
for i in lst.__reversed__():
    print(i)  # 1, 2
# __setitem__(p, e)  # s[p] = e - e 를 p 위치에 저장하고, 기존 항목을 덮어쓴다.
lst.__setitem__(1, 99)  # [1, 2] -> [1, 99]
# sort([key], [reverse]) # 선택적인 키워드 key 와 reverse 에 따라 항목을 정렬하고 s 에 저장한다.
lst.sort(key=None, reverse=True) # 내림차순
