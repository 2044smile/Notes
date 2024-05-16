# 3.4 융통성 있게 키를 조회하는 매핑
## 검색할 때 키가 존재하지 않으면 어떤 특별한 값을 반환하는 매핑이 있으면 편리한 때까지 종종 있다.
## 하나는 평범한 dict 대신 defaultdict를 사용하는 방법
## 다른 하나는 dict 등의 매핑형을 상속해서 __missing__() 메서드를 추가하는 방법이다.
