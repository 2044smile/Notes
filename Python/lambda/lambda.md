## Python lambda

### Basic example

```python
lambda x : x + 1

(lambda x: x + 1)(2)  # 3

add_one = lambda x: x + 1
add_one(2)  # 3

# multiple arguments
full_name = lambda first, last: f"Full name: {first.title()} {last.title()}"
full_name('guido', 'van rossum')
```

### Anonymous Function

```python
lambda x, y: x + y
_(1, 2)  # 3

# Immediately Invoked Function Expression(IIFE, pronounce "iffy")
(lambda x, y: x + y)(2, 3) # 5

high_ord_func = lambda x, func: x + func(x)
high_ord_func(2, lambda x: x * x)  # 6
high_ord_func(2, lambda x: x + 3)  # 7
```

Python exposes higher-order functions as built-in functions or in the standard library.

Examples include map(), filter(), functools.reduce(), as well as key functions like sort(), sorted(), min(), and max().

### Single Expression

```python
(lambda x:
(x % 2 and 'odd' or 'even'))(3)  # odd
```

### No Statements

lambda 함수 내에서 return, pass, assert, or raise와 같은 statements들은 포함될 수 없다.

포함되면 SyntaxError exception 발생

### Type Annotations

basic func에서는 Python Type Checking이 가능하지만 lambda 안에서는 불가능하고, SyntaxError exception 발생

```python
# basic
def full_name(first: str, last: str) -> str:
    return f"{first.title()} {last.title()}"

# lambda
lambda first: str, last: str: first.title() + " " + last.title() -> str
```

### Arguments

def로 정의된 정규 함수 개체와 마찬가지로 Python lambda식은 인수로 전달하는 모든 다양항 방법을 지원합니다.

```python
(lambda x, y, z: x + y + z)(1, 2, 3)  # 6

(lambda x, y, z=3: x + y + z)(1, 2)  # 6

(lambda x, y, z=3: x + y + z)(1, y=2)  # 6

(lambda *args: sum(args))(1,2,3)  # 6

(lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)  # 6

(lambda x, *, y=0, z=0: x + y + z)(x=1, y=2, z=3)
```

## Reference
https://realpython.com/python-lambda/
