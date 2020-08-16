# Input

## 연속 된 5개의 데이터 받기

```python
# 입력: 1 2 3 4 5
# input().split() -> ['1', '2', '3', '4', '5']
# map(int, input().split()) -> map([1,2,3,4,5])

a, b, c, d, e = map(int, inpit().split())

a = list(map(int, inpit().split()))
```

## 빠르게 입력 받기

- 그래프나 입력이 많은 경우에 사용합니다.

```python
import sys

data = sys.stdin.readline().rstrip()
print(data)
```
