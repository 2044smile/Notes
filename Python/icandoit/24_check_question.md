# if 조건문을 효울적으로 사용하기

```python
grade = float(input("> 학점을 입력해주세요: "))

print("타이밍이 귀찮다... 윤인성 유튜브를 보자")

x = 10
y = 2

if x > 4:  # 10 > 4 true
    if y > 2:  # 2 > 2 false
        print(x * y)
    # else 케이스가 없기 떄문에 출력하지 않는다.
else:
    print(x + y)

if x > 10:
    if x < 20:
        print("조건에 맞습니다")
# 변경
if (x > 10) and (x < 20):
    print("조건에 맞습니다")
```