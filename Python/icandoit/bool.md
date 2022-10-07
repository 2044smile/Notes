# 불 자료형

True, False 두 개만 만들 수 있다.

# 비교 연산자
## = 할당 연산자
## == 비교 연산자

```python
10 == 20
False

10 != 20
True

10 < 20
True

10 <= 20
True

10 > 20
False

10 >= 20
False

"apple" < "banana"  # a 가 제일 작고, z가 제일 크다. 
True

10 < 20 < 30
True

x = 20
10 < x < 30
True
```

# 논리 연산자
## 단항 not
```python
not True  # False
not False  # True

"1020".isalnum()  # 영어, 한글, 숫자 True
True
not "1020".isalnum()
False
```
## 이항 and
### 둘 다 True 일 때 결과 True
```python
True and True  # True
True and False  # False
False and True  # False
False and False  # False
```

## 이항 or
### 둘 중 하나가 True이면 결과 True
```python
True or True  # True
True or False  # True
False or True  # True
False or False  # True
```
