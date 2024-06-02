# 3.6 UserDict 상속하기
## dict 보다는 UserDict 를 상속해서 매핑형을 만드는 것이 쉽다.
## 내장형에서는 아무런 문제없이 상속할 수 있는 메서드들을 오버라이드해야 하는 구현의 특이성 때문에 dict 보다는 UserDict 를 상속하는 것이 낫다.
from collections import UserDict


class StrKeyDict(UserDict):
    def __missing__(self, key):
        if isinstance(key, str):  # key 가 없을 때 발생하는 에러
            raise KeyError(key)
        return self[str(key)]  # `키가 있다면 문자열로 변경`
    
    def __contains__(self, key):  # in 연산자를 호출할 때 자동으로 사용 / 저장된 키가 모두 str 형이므로 self.data 로 바로 조회할 수 있다.
        return str(key) in self.data
    
    def __setitem__(self, key, item):  # e.g) [1,2,3] __setitem__(-1, 99) -> [1,2,99]
        self.data[str(key)] = item
