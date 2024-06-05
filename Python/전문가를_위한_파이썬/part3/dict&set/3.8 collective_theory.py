# 집합(set) 이론
## 집합(set)은 고유한 객체의 모음으로서, `기본적으로 중복 항목을 제거한다.`
l = ['spam', 'eggs', 'spam', 'eggs']
set(l)  # {'eggs', 'spam'}
list(set(l))  # ['eggs', 'spam']

## 집합 요소는 반드시 해시할 수 있어야 한다.
## set은 해시 가능하지 않지만 frozenset은 해시 가능하므로, frozenset이 set에 들어갈 수 있다.

# TMI
## `list` 의 경우 hash 를 사용하지 않기 때문에 메모리를 적게 사용한다.
### 그리고 구현 특성 상 list 가 단순하여 iteration(반복)이 더 빠르다. / 메모리 측면에서 list 가 적게 쓴다.
### `list` 특히 `array list` 쓰는 것을 추천한다.
## `set` 의 경우 전체를 한번씩 확인을 해야 한다 그래서 overhead 가 발생한다. 즉 iteration(반복) 이 느리다.
### 메모리 사용 비용 증가

## set 은 기본적인 집합 연산을 구현한다.
### | 합집합, & 교집합, - 차집합
a = set([1,2,3])
b = set([3,4,5])

### 합집합
print(a | b)  # 1,2,3,4,5
print(len(a | b))  # 5

### 교집합
print(a & b)  # 3
print(len(a & b))  # 1

### 차집합
print(a - b)  # 1, 2
print(b - a)  # 4, 5
