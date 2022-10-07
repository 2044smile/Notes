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

### 예시
```python
# 예1.

# 어린이날에 호텔에서
# "호텔 멤버쉽 회원" 이면서
# "12세 이하의 어린이 동반"
# -> Gift(선물)
# is멤버쉽 and is어린이동반

# 예2.

# 배달 음식 애플리케이션에서
# "주문한 음식 가격 2만원 이상" 이면서
# "거리 500m 이하의 경우"
# -> Free(무료)
# -> (가격 >= 20000) and (거리 <= 500)

# 예3.

# 쇼핑몰에서
# "우리카드" 와 "신한카드"
# -> interest-free(무이자)
# -> is우리카드() or is신한카드()

# 예4.

# 주차장에서
# "전기자동차"와 "하이브리드자동차"
# -> a-parking-pee(주차비) Discount(할인)
# -> is전기차() or is하이브리드차()
```


