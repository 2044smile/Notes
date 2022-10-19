# if~else와 elif 구문

## if 조건문 복습

### 홀수 짝수 구분
```python
# 기본
number = int(input("정수 입력: "))
if number % 2 == 0:
    print("짝수입니다.")
if number % 2 == 1:
    print("홀수입니다.")

# Lambda 사용
a = int(input("숫자를 입력해주세요: "))

f = lambda a: "짝수이다" if a % 2 == 0 else "홀수이다"
print(f)
```

### 오전 오후 구분
```python
from pytz import timezone
from datetime import datetime

today = datetime.now(timezone('Asia/Seoul'))
today.hour
if today.hour < 12:
    print("오전")
if today.hour >= 12:
    print("오후")
```

## elif

```python
number = int(input("정수 입력: ))

if number > 0:
    print("양수")
elif number < 0:
    print("음수")
else:
    print("0 입니다")
```

Python Tutor에서 양수, 음수, 0일 때 어떻게 타고 가는지 살펴보자.