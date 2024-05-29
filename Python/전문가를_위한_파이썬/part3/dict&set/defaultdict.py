# 3.4 융통성 있게 키를 조회하는 매핑
## 검색할 때 키가 존재하지 않으면 어떤 특별한 값을 반환하는 매핑이 있으면 편리한 때까지 종종 있다.
## 하나는 평범한 dict 대신 defaultdict를 사용하는 방법
## 다른 하나는 dict 등의 매핑형을 상속해서 __missing__() 메서드를 추가하는 방법이다.

# 3.4.1 defaultdict: 존재하지 않는 키에 대한 또 다른 처리
## collections.defaultdict 는 존재하지 않는 키로 검색할 때 요청에 따라 항목을 생성하도록 설정되어 있다.
## 작동 방식은 defaultdict 객체를 생성할 때 존재하지 않는 키 인수로 __getitem__() 메서드를 호출할 때 마다 기본값을 생성하기 위해 사용되는 콜러블을 제공
import sys
import re
import collections

WORD_RE = re.compile('\w+')

index = collections.defaultdict(list)  # list 생성자를 갖고 있는 defaultdict 생성
with open(sys.argv[0], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            index[word].append(location)  # word 가 index 에 들어 있지 않으면 default_factory 를 호출해서 없는 값에 대한 항목을 생성하는데
            # 여기서는 빈 리스트를 생성(collections.defaultdict(list)) 해서 index[word] 에 할당한 후 반환하므로, append(location) 연산은 언제나 성공한다.

# print in alphabetical order
for word in sorted(index, key=str.upper):
    print(word, index[word])

# 3.4.2 __missing__() 메서드
## 매핑형은 이름으로도 쉽게 추측할 수 있는 __missing__() 메서드를 이용해서 존재하지 않는 키를 처리한다.
##* 이 특수 메서드는 기본 클래스인 dict에는 정의되어 있지 않지만, dict는 이 메서드를 알고 있다.
## 따라서 dict 클래스를 상속하고 __missing__() 메서드를 정의하면, dict.__getitem__() 표준 메서드가 키를 발견할 수 없을 때 KeyError 를 발생시키지 않고, __missing__() 메서드를 호출한다.
### 간단한 방법은 .get('c', None)
### simple is best
dic = {'a':'a', 'b':'b', 'd':'d'}
dic['c']  # KeyError: 'c'

class Dict(dict):
    def __missing__(self, name):
        return "BEEP"


target = Dict({'a':'a', 'b':'b', 'd':'d'})
print(target['c'])  # 'BEEP'

class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default
        
    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

target.get('c', None)

# 3.7 조회할 때 키를 문자열로 변환하는 StrKeyDict()
## StrKeyDict0 클래스는 키를 숫자 또는 문자열로 저장하고 검색할 수 있도록 유연하게 처리합니다.
class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):  # 키가 문자열인지 확인한다. 키가 문자열이고 존재하지 않으면 KeyError 가 발생한다.
            raise KeyError(key)
        return self[str(key)]  # 키에서 문자열을 만들고 조회한다.
    
    def get(self, key, default=None):  # get() method 는 self[key] 표기법을 이용해서 `__getitem__()` 메서드에 위임한다. 이렇게 함으로써 __missing__() 메서드가 작동할 수 있는 기회를 준다.
        try:
            return self[key]
        except KeyError:
            return default
        
    def __contains__(self, key):  # 객체가 특정 키를 포함하고 있는지를 확인하는 데 사용 / 이 메서드는 `in` 연산자가 호출될 떄 자동으로 호출
        return key in self.keys() or str(key) in self.keys()  # 수정하지 않은 (문자열이 아닐 수 있는) 키를 검색하고 나서, 키에서 만든 문자열로 검색한다.
        # 재귀적 호출 문제를 피하기 위해 여기서는 key in self.keys() 와 같이 명시적으로 키를 조회
        # 아주 큰 매핑의 경우에도 k in dict.keys() 형태의 검색이 효율적이다. dict.keys() 는 집합과 비슷한 뷰를 반환하는데, 집합에 포함되었는지 여부를 검사하는 것은 딕셔너리만큼 빠르기 떄문이다.


dic = {"a":"a", "b": "b", "d":"d", "1":"1"}
d = StrKeyDict0(dic)
d["a"]  # 'a'
d[1]  # KeyError __missing__()
## __contains__
print(1 in d)  # True
print('1' in d)  # True

# 3.5 그 외 매핑형
## 표준 라이브러리의 collections 모듈에서 제공하는 여러 매핑형을 간단히 살펴본다.

## collections.OrderedDict
### 키를 삽입한 순서대로 유지함으로써 항목을 반복하는 순서를 예측할 수 있다.
### OrderedDict 의 popitem() 메서드는 기본적으로 최근에 삽입한 항목을 꺼내지만, my_odict.popitem(last=True) 형태로 호출하면 처음 삽입한 항목을 꺼낸다.
from collections import OrderedDict, ChainMap, Counter

odict = OrderedDict({"a": "A", "b": "B", "c": "C"})
print(odict)  # OrderedDict([('a', 'A'), ('b', 'B'), ('c', 'C')])
odict.popitem()  # ('c', 'C')
odict.popitem(last=False)  # ('a', 'A')

## collections.ChainMap
### 매핑들의 목록을 담고 있으며 한꺼번에 모두 검색할 수 있다.
### 각 매핑을 차례대로 검색하고, 그중 하나에서라도 키가 검색되면 성공한다.

### 업데이트 처리, Multi threading 환경에서 race condition이 발생될 수 있으며, 관리해야 할 객체가 늘어나게 되었다. 또한, 키값이 동일한 경우 값이 덮어쓰기된다.
d1 = {"A1": 1, "A2": 2, "A3": 3}
d2 = {"A2": 20, "A4": 40}

combined1 = d1 | d2
print(combined1)  # {'A1': 1, 'A2': 20, 'A3': 3, 'A4': 40}

### ChainMap은 다수의 dictionary를 비롯한 여러가지 객체를 논리적으로 맵핑 및 그룹화하여 하나로 동작하게 되어 원본 객체 데이터의 view를 생성한다.
### ChainMap으로 생성한 데이터는 원본데이터를 가지고 신규로 생성한 데이터를 갖는것이 아닌, 원본데이터를 보여줄 수 있도록 참조하는 것이며, 원본데이터가 변경되는 경우 ChainMap 객체에서 표시되는 데이터는 변경된 원본데이터를 계속해서 참조하기 때문에 동일하게 변경되는 것 처럼 보이게 된다.
### 정의된 dictionary를 통합하여 검색할 수 있으며, 같은 key가 존재하는 경우 `첫번째 mapping list의 객체의 key값이 반환된다.`
combined2 = ChainMap(d1, d2)
print(combined2)  # ChainMap({'A1': 1, 'A2': 2, 'A3': 3}, {'A2': 20, 'A4': 40})
print(combined2['A1'])  # 1
print(combined2['A2'])  # 2

### 내부적으로 관리되는 mapping 목록을 통해 원본 객체에 접근할 수 있다. 
combined2.maps[0]  # {'A1': 1, 'A2': 2, 'A3': 3}
combined2.maps[1]  # {'A2': 20, 'A4': 40}
print(id(d1))  # 139821075654784 same
print(id(combined2.maps[0]))  # 139821075654784 same
print(id(d2))
print(id(combined2.maps[1]))
### 키가 겹치지 않는다는 가정의 dict 들에서 합칠 때 용이하다.

## collections.Counter
ct = Counter('akdjflkasjv')
print(ct)  # Counter({'a': 2, 'k': 2, 'j': 2, 'd': 1, 'f': 1, 'l': 1, 's': 1, 'v': 1})
ct.update('aaaaaaaavvvvvvvv')
print(ct)  # {'a': 10, 'v': 9, 'k': 2, 'j': 2, 'd': 1, 'f': 1, 'l': 1, 's': 1}
ct.most_common(2)  # [('a', 10), ('v', 9)]
