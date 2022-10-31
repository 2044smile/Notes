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

## 문제

```python
# 1-1번
dict_a = {}
dict_a['name'] = "구름"
print(dict_a)  # {"name": "구름"}

# 1-2번
dict_a = {"name": "구름"}
del dict_a["name"]
print(dict_a)  # {}

# 2번
pets = [
    {"name": "구름", "age": 5},
    {"name": "초코", "age": 3},
    {"name": "아지", "age": 1},
    {"name": "호랑이", "age": 1}
]

print("# 우리 동네 애완 동물들")
for pet in pets:
    print(f"{pet['name']} {pet['age']}살")
```