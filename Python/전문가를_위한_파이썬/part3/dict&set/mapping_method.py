# 3.3 공통적인 매핑 메서드
## dict와 dict의 변형 중 가장 널리 사용되는 defaultdict와 OrderDict 클래스
## dict, collections.defaultdict, collections.OrderDict 매핑형의 메서드
## OrderDict.popitem()은 최근에 삽입된 항모글 제거한다. (LIFO)
## 선택적 인수 last 를 False 로 설정하면 처음에 삽입된 항목을 제거한다. (FIFO)
### d.update({key: value}) 덕 타이핑
### setdefault(): 똑같은 키를 여러 번 조회하지 않게 해줌으로써 속도를 엄청나게 향상시킨다.
#### d.setdefault('name') 만약 'name' 키가 존재한다면 그 값을 출력하고, 없다면 키를 생성하고, value 는 None 으로 대입

# 3.3.1 존재하지 않는 키를 setdefault() 로 처리하기
## 존재하지 않는 키 k로 d[k]를 접근하면 dict 는 오류를 발생시킨다.
## KeyError 를 처리하는 것 보다 기본값을 사용하는 것이 더 편리한 경우에는 d[k] 대신 d.get(k, None) 을 사용한다.
### d.get('name', None) -> 'cslee'
## 그렇지만 발견한 값을 갱신할 때 해당 객체가 가변 객체면 __getitem__() 이나 get() 메서드는 보기 어색하며, 효율성도 떨어진다.
# BEGIN INDEX0
"""Build an index mapping word -> list of occurrences"""

import sys
import re

WORD_RE = re.compile('\w+')

index = {}
with open(sys.argv[0], encoding='utf-8') as fp:  # ipython3
    """
    #!/usr/bin/python3
    # -*- coding: utf-8 -*-
    import re
    import sys
    from IPython import start_ipython
    if __name__ == '__main__':
        sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
        sys.exit(start_ipython())
    """
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):  # finditer 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 돌려준다.
            """
            <re.Match object; span=(3, 6), match='usr'>
            <re.Match object; span=(7, 10), match='bin'>
            <re.Match object; span=(11, 18), match='python3'>
            <re.Match object; span=(6, 12), match='coding'>
            <re.Match object; span=(14, 17), match='utf'>
            <re.Match object; span=(18, 19), match='8'>
            <re.Match object; span=(0, 6), match='import'>
            <re.Match object; span=(7, 9), match='re'>
            """
            word = match.group()
            """
            usr
            bin
            python3
            coding
            utf
            8
            """
            column_no = match.start()+1
            """
            span=(`3`, 6),   3 + 1 = 4  -> 3이 의미하는 건 인덱스 #!/`u`s`r`/`b`i`n`/`p`ython`3`
            span=(`7`, 10),  7 + 1 = 8
            span=(`11`, 18)  11 + 1 = 12
            """
            location = (line_no, column_no)
            """
            #!/usr/bin/python3
            (1, 4)  usr
            (1, 8)  bin
            (1, 12) python3 
            (2, 7)  coding
            (2, 15) utf
            """
            # this is ugly; coded like this to make a point
            # Bad case
                # occurrences = index.get(word, [])  # <1>
                # occurrences.append(location)       # <2>
                # index[word] = occurrences          # <3>
        # Good
            index.setdefault(word, []).append(location)  # 예제 3-4 occurrences 처리하는 코드 세 줄을 setdefault 를 이용하면 한 줄로 변경 가능
            # 단어에 대한 occurrences 리스트를 가져오거나, 단어가 없을 때는 빈 배열 ([]) 을 가져온다.
            # setdefault() 가 값을 반환하므로 한 번 더 검색할 필요 없이 갱신할 수 있다.
            # Bad case
                # if key not in my_dict:
                #     my_dict[key] = []
                # my_dict[key].append(new_value)

# print in alphabetical order
for word in sorted(index, key=str.upper):  # <4> str.upper() 를 사용하지 않고, str.upper 를 입력해서 함수에 대한 참조를 전달하면 된다.
    """
    0 [(7, 14), (7, 66)]
    8 [(2, 19)]
    argv [(7, 9), (7, 61)]
    bin [(1, 8)]
    coding [(2, 7)]
    exe [(7, 44)]
    exit [(8, 9)]
    from [(5, 1)]
    if [(6, 1)]
    import [(3, 1), (4, 1), (5, 14)]
    IPython [(5, 6)]
    python3 [(1, 12)]
    pyw [(7, 38)]
    r [(7, 26)]
    re [(3, 8), (7, 19)]
    script [(7, 30)]
    start_ipython [(5, 21), (8, 14)]
    sub [(7, 22)]
    sys [(4, 8), (7, 5), (7, 57), (8, 5)]
    usr [(1, 4)]
    utf [(2, 15)]
    __main__ [(6, 17)]
    __name__ [(6, 4)]
    """
    print(word, index[word])
# END INDEX0
