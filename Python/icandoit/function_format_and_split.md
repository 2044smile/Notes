# format 함수와 split 함수

```python
a = 52
b = 273

print(a + "+" + b + "=" + (a + b)) # TypeError 발생 문자열과 숫자
```

## format 함수(자동으로 문자열로)
```python
print("{}".format(10))
print("{}년{}월{}일".format(2022, 10, 1))
print("{} + {} = {}".format(a, b, a + b))
```

## f-문자열
```python
a = 10
b = 20
print(f"{a} + {b} = {a + b}")

f"""{a} + {b} = {a + b}
{a} - {b} = {a - b}
{a} * {b} = {a * b}
{a} / {b} = {a / b}"""
``` 

## split 함수
```python
"10 20 30 40".split(" ")
"10-20-30-40".split("-")
# ['10', '20', '30', '40'] list
```
