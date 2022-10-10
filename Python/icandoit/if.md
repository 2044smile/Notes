# if 조건문
## 조건이 True일 때만 들여쓰기 안쪽의 문장을 실행
```python
if True:
    print("True")

if False:
    print("False")  # 실행되지 않는다.
```
## 사용자가 입력한 숫자가 양수 음수 0인지 판별하는 프로그램
```python
a = input("정수를 입력해주세요: ")
a = int(a)

if a > 0:
    print("양수입니다.")
elif a < 0:
    print("음수입니다.)
else:
    print("0 입니다.")
```
## 오전 오후 구분하는 프로그램
```python
from pytz import timezone
from datetime import datetime


today = datetime.now(timezone('Asia/Seoul'))

print(f"{today.hour}시 입니다.)

if today.hour < 12:
    print("오전입니다.")
else:
    print("오후입니다.")


## 계절을 구분하는 프로그램
from pytz import timezone
from datetime from datetime

today = datetime.now(timezone('Asia/Seoul'))
m = today.month

if 3 <= m <= 5:
    print("봄 입니다.")
elif 6 <= m <= 8:
    print("여름 입니다.")
elif 9 <= m <= 11:
    print("가을 입니다.")
elif 11 <= m <= 12 or (m == 1):
    print("겨울 입니다.")
```
## 복합 문장: 문장을 묶어 놓은 것
```python
if 조건: 복합 문장

들여쓰기를 함으로써 복합 문장이라는 것을 알린다.

print('A')
if False:
    print('B')
print('C')
print('D')
```
