# 리스트 함수

# 파괴적이다: 연산 후에도 피연산자가 번형되지 않는 것
## = 할당 연산자
```python
a = 10
print(a) # a = 10

a = 20
print(a) # a = 20
```

# 비파괴적이다: 연산 후에도 피연산자가 변형되지 않는 것
## +-*/ 연산자
## 장점: 원본과 결과가 모두 남는다. -> 안전하다.
## 단점: 원본과 결과가 둘 다 남긴다. -> 메모리를 많이 차지한다.
```python
a = 10
print(a) # a = 10
a + 20
print(a) # a = 10
b = a + 20
print(b) # b = 30
```

###  리스트는 크기가 클 가능성이 높으므로 비파괴적으로 원본과 결과를 모두 남기기에는 -> 메모리 용량을 압박할 가능성이 있습니다. ! 그래서 파괴적 연산을 사용합니다.

# 리스트의 함수는 모두 다 파괴적으로 동작합니다.
## 요소 추가: append(), insert(), extend()
```python
a = [1, 2, 3, 4]
a.append(10) # 가장 마지막에 요소를 하나 추가
print(a)
a.insert(0, 99) # 원하는 위치에 요소를 하나 추가
print(a)
a.extend([5,6,7,8]) # 가장 마지막에 요소를 여러 개 추가
print(a)
# same
a = a + [5,6,7,8]
# 파괴적함수이기 때문에 a = a.append(99) X
# a.append([5,6,7,8]) -> [1,2,3,4 [5,6,7,8]]
```
## 요소 제거: del, pop(), remove(), clear()
```python
a = [1,2,3]
del a[0]  # 제거하고 싶은 인덱스 입력
print(a)  # [2,3]
a.pop(0)  # 제거하고 싶은 인덱스 입력(기본값 -1) 마지막부터 삭제
print(a)  # [3]
a.remove(3)  # 제거하고 싶은 요소를 입력
print(a)  # []
a.clear()  # 전부 제거
print(a)  # []
```
## 요소 정렬: sort()
```python
a = [5, 66, 22, 99, 11, 0]
a.sort()  # 파괴적 함수이기 때문에 a = a.sort() 할 필요 없다.
print(a)  # 오름차순, [0, 5, 11, 22, 66, 99]
a.sort(reverse=True)
print(a)  # 내림차순, [99, 66, 22, 11, 5, 0]
```

## 요소 존재를 확인: in, not in
```python
# 영어는 "in 뒤에 큰 것"이 옵니다.
# 연필 in 상자
# 강아지 in 공원
print(5 in a)  # True
print(100 in a)  # False
print(5 not in a)  # False
print(100 not in a)  # True
```