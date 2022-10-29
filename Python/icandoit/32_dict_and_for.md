# 딕셔너리와 반복문

## 마트에서 어떤 제품 관리
```python
product = [
    ['건망고 슬라이스', 4000, '식품'],
    ['인스타360 링크', 140000],
    ['와콤 프로펜', 15000]
]
product[0][0]
product[0][1]
```

## 딕셔너리 탄생
```python
product = {
    '제품명': 'cslee',
    '가격': '100000000000000',
    '분류': 'human'
}

product['제품명']  # cslee
product['가격']  # 4000
product['분류']  # human


# {}를 사용
# "키: 값" 쌍을 여러 개 입력
# 키: 숫자, 문자열, 불(, 튜플)
# 값: 모든 값

# 딕셔너리와 for 반복문

for key in product:
    print(key)  # Key
    print(product[key])  # Value
```