# List

## Python_ListComprehension_2차원

- 작성 예정

## for loop (_) 의미

- 변수를 사용하지 않을 때 _로 대체

```python
for _ in range(10):
    print('Hello World')
```

## sort vs sorted

```python
a = [5, 4, 3, 9, 10]
a.sort()
```

print(a) 값 자체를 바로 변경시킨다.

```python
b = [5, 4, 3, 9, 10]
result = sorted(b)  # 내장함수

print(b) # 5, 4, 3, 9, 10
print(result) # 3, 4, 5, 9, 10
```

## remove

- remove 는 전체 삭제를 지원하지 않는다. 그래서 아래와 같은 예시를 사용하여 삭제한다.

```python
a = [5, 2, 4, 6, 8, 4]
remove_set = {3, 5} # Set

result = [i for i in a if i not in remove_set]

print(result) # [1, 2, 4]
```
