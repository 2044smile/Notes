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
