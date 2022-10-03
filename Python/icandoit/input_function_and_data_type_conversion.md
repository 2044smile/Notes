# input() 함수
prompt: 입력을 요청하는 문자열
```python
print(input("입력해주세요: "))
# 함수의 결과 = 함수의 리턴 값

a = input(">>> ")
print(a)
print(type(a)) # <class 'str>

# input() 함수의 결과는 "무조건" **문자열**이다.

a = input("숫자1: ")
b = input("숫자2: ")

print(a + b) # 1020 이유는 문자열을 더하기 때문이다. 그렇다면 int형으로 연산하려면?

print(int(a) + int(b)) # 요렇게 해주면 된다. 

int("52") # 정수
float("52.273") # 부동소수점
str(52) # 숫자 -> 문자열

# 예외
int("hello")
int("52.273")
```