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