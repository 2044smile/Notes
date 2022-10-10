# 파괴적 연산과 비파괴적 연산

```python
a = 10

# + 연산자: 피연산자를 바꾸지 않음
# 비파괴적
a + 10
a + 20
a + 30
a + a

# = 연산자: 피연산자를 바꿈!
# 파괴적 - 그냥 평상 시 많이 사용한다.
a = a + 10
a = 20
a = 30

print(a) # 30
```

# upper and lower (대문자 and 소문자)

```python
a = "hEllO PyThOn"

a.upper() # 대문자로 변경
a.lower() # 소문자로 변경

print(a) # 비파괴적

a = a.upper() # 파괴적
print(a)
a = a.lower()
print(a)
```

# strip (공백제거)

```python
a = "    Hi \n\t  "
a = a.strip()
print(a)
a = a.lstrip()
a = a.rstrip()
```

# is func(is 로 시작하면 True, False 결과)

```python
a = "   안녕하세요   "
print(a.isalpha()) # False
a = "abcd"
print(a.isalpha()) # True

a = " Hello "
a = a.strip().isalpha() # True
```

# find and rfind

```python
# 왼쪽부터 탐색
find()

# 오른쪽부터 탐색
rfind()

a = "abcdabcd"
a.find("b") # 1
a.rfind("b") # 5 오른쪽 부터 읽어도 리스트의 순서는 변함이 없다.
a.find("z") # 없는 값은 -1 을 출력한다.
```

# in 연산자 (문자열 내부에 문자열이 있는지 확인)

```python
print("안녕" in "안녕하세요") # True
print("잘가" in "안녕하세요") # False
```

# format() 함수 고급

```python
# 정수
"{:d}".format(52)

## '특정 칸만큼' 출력 
"{:5d}".format(52)
"{:10d}".format(52)

## 빈칸을 '0'으로 채운다
"{:05d}".format(52)
"{:010d}".format(52)

## 부호
"{:5d}".format(52)
"{:5d}".format(-52)
"{:=5d}".format(52)
"{:=5d}".format(-52) # - 부호가 앞으로 밀려서 출력
"{:+5d}".format(52) # + 가 붙는다
"{:+5d}".format(-52) # +지만 format 내부에 -로 지정되어 있다.
"{:=+5d}".format(52) # + 부호가 앞으로 밀려서 출력
"{:=+5d}".format(-52)

# 부동소수점, f = float
"{:f}".format(52)

## 부호
"{:=+20f}".format(52)
"{:=+20f}".format(-52)
"{:=+20.1f}".format(52)
"{:=+20.2f}".format(52)
"{:=+20.3f}".format(52)
### 자주 사용할 듯 ###
"{:=.1f}".format(52.123) # 52.1
"{:=.2f}".format(52.123) # 52.12
"{:=.3f}".format(52.123) # 52.123

### 내용 추가
"My name is {0:<10}".format('left')  # 왼쪽 정렬
# 'My name is left      '
"My name is {0:>10}".format('right')  # 오른쪽 정렬
# 'My name is      right
"My name is {0:^10}".format('center')  # 가운데 정렬
# 'My name is   center  '
```