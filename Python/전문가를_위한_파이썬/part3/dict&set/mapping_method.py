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
