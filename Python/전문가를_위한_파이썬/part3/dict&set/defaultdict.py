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
    
    def get(self, key, default=None):  # get() method 는 self[key] 표기법을 이용해서 __getitem__() 메서드에 위임한다. 이렇게 함으로써 __missing__() 메서드가 작동할 수 있는 기회를 준다.
        try:
            return self[key]
        except KeyError:
            return default
        
    def __contains__(self, key):  # 객체가 특정 키를 포함하고 있는지를 확인하는 데 사용 / 이 메서드는 `in` 연산자가 호출될 떄 자동으로 호출
        return key in self.keys() or str(key) in self.keys()  # 수정하지 않은 (문자열이 아닐 수 있는) 키를 검색하고 나서, 키에서 만든 문자열로 검색한다.


dic = {"a":"a", "b": "b", "d":"d", "1":"1"}
d = StrKeyDict0(dic)
d["a"]  # 'a'
d[1]  # KeyError __missing__()
## __contains__
print(1 in d)  # True
print('1' in d)  # True
