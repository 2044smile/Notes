# 딕셔너리의 요소 변경/추가/제거

```python
product = {
    "name": "7D 건조 망고",
    "type": "당절임"
}

print(product)

# 요소에 값을 변경하는 방법
product["name"] = "8D 건조 망고"

# 요소를 추가하는 방법
product["price"] = 4000

# 요소를 제거하는 방법
del product["type"]

# 키의 존재 확인하는 방법
product["price"]  # KeyError: 'price'
"price" in product  # True or False
if "price" in product:
    print(product["price"])
else:
    print("키가 존재하지 않습니다")

# get()
product.get("name")
# 존재하지 않는 값을 입력했을 때는 오류를 발생하지 않고 None을 출력한다.
```