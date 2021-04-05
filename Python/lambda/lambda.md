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

### Decorator

함수를 받아 명령을 추가한 뒤 이를 다시 함수의 형태로 반환하는 함수이다.

**함수의 내부를 수정하지 않고 기능에 변화를 주고 싶을 때 사용한다.**

일반적으로 함수의 전처리나 후처리에 대한 필요가 있을 때 사용한다.

또한 데코레이터를 이용해, 반복을 줄이고 메소드나 함수의 책임을 확장한다.

**Decorator Structure**
```python
def out_func(func):  # 기능을 추가 할 함수를 인자로
    def inner_func(*args, **kwargs):
        return func(*args, **kwargs)
    return inner_func
```
**example.py**
```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print('전처리')
        print(func(*args, **kwargs))
        print('후처리')
        return wrapper
    return decorator

@decorator
def example():
    return 'func'

example()
''''''''''
전처리
func
후처리
''''''''''
```

**클래스로 만드는 Decorator Structure**
```python
class Decorator:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)
```
**example.py**
```python
class Decorator:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print('전처리')
        print(self.func(*args, **kwargs))
        print('후처리')

@Decorator
def example():
    return 'Class'

example()
''''''''''
전처리
Class
후처리
''''''''''
```

**lambda Decorator example**
```python
# Defining a decorator
def trace(f):
    def wrap(*args, **kwargs):
        print(f"[TRACE] func: {f.__name__}, args: {args}, kwargs: {kwargs}")
        return f(*args, **kwargs)

    return wrap

# Applying decorator to a function
@trace
def add_two(x):
    return x + 2

# Calling the decorated function
add_two(3)

# Applying decorator to a lambda
print((trace(lambda x: x ** 2))(3))
''''''''''
[TRACE] func: add_two, args: (3,), kwargs: {}
[TRACE] func: <lambda>, args: (3,), kwargs: {}
9
''''''''''
```

람다의 경우엔 <lambda>로 함수명이 출력되는 것을 확인할 수 있다.

이러한 방식으로 람다 함수에 데코레이터를 사용하면 디버깅이 유용하고, higher-order function 또는 key function의 컨텍스트에서 사용되는 람다 함수의 동작을 디버깅하는 데 유용 할 수 있다.

**lambda Decorator example - map()**
```python
list(map(trace(lambda x: x*2, range(3)))
''''''''''
[TRACE] Calling <lambda> with args (0,) and kwargs {}
[TRACE] Calling <lambda> with args (1,) and kwargs {}
[TRACE] Calling <lambda> with args (2,) and kwargs {}
[0, 2, 4]
''''''''''
```

하지만 람다에 데코레이터를 사용하는 것은 PEP 8 에서 권장하지 않는다고 합니다.
이와 관련 된 정보는 링크 를 눌러 확인해보세요.https://www.python.org/dev/peps/pep-0008/#programming-recommendations

### Closure

프로그래밍 언어에서의 클로저란 퍼스트클래스 함수를 지원하는 언어의 네임 바인딩 기술이다. 클로저는 어떤 함수를 함수 자신이 가지고 있는 환경과 함께 저장한 레코드이다. 또한 함수가 가진 프리변수(free variable)를 클로저가 만들어지는 당시의 값과 레퍼런스에 맵핑하여 주는 역할을 한다. 클로저는 일반 함수와는 다르게, 자신의 영역 밖에서 호출된 함수의 변수값과 레퍼런스를 복사하고 저장한 뒤, 이 캡처한 값들에 액세스할 수 있게 도와준다.

```python
def outer_func(x):
    y = 4
    def inner_func(z):
        print(f"x = {x}, y = {y}, z = {z}")
        return x + y + z
    return inner_func

for i in range(3):
    closure = outer_func(i)
    print(f"closure({i+5}) = {closure(i+5)})

''''''''''
x = 0, y = 4, z = 5
closure(5) = 9
x = 1, y = 4, z = 6
closure(6) = 11
x = 2, y = 4, z = 7
closure(7) = 13
''''''''''
```

**lambda Closure example**

```python
def outer_func(x):
    y = 4
    return lambda z: x + y + z

for i in range(3):
    closure = outer_func(i)
    print(f"closure({i+5}) = {closure(i+5)})

''''''''''
closure(5) = 9
closure(6) = 11
closure(7) = 13
''''''''''
```

이 경우 정상 함수와 람마 도무 비슷하게 작동합니다. 다음 섹션에서는 람다의 평가 시간(정의 시간 대 런타임)으로 인해 람다의 동작이 기만적일 수 있는 상황을 볼 수 있습니다.

### Evaluation Time

Loop와 관련 된 일부 상황에서는 파이썬 람다 함수의 Closure 동작이 직관적이지 않을 수 있습니다. 자유 변수(free variables)가 람다의 컨텍스트에서 바인딩된 경우를 이해해야 합니다.

```python
def wrap(n):
    def f():
        print(n)
    return f

numbers = 'one', 'two', 'three'
funcs = []
for n in numbers:
    funcs.append(wrap(n))

for f in funcs:
    f()

''''''''''
one
two
three
''''''''''
```

**lambda Evaluation Time example**
```python
numbers = 'one', 'two', 'three'
funcs = []
for n in numbers:
    funcs.append(lambda: print(n))

for f in funcs:
    f()

''''''''''
three
three
three
''''''''''
```

위 예시의 결과를 보면 정말 이상하다, three가 3개가 나오고 있다.

여기서 내가 검색하거나 주변분들에게 물어 얻은 답은 아래와 같다.

- lambda 동작 방식이 heap과 연관되어 있다. 호출이 끝나면 heap에서 빠져나온다. 예제를 보면 현재 lambda는 print를 출력하고 있다. 근데 funcs 배열에 넣을 때 lambda가 현재 콜은 안하고 함수 객체 상태로 들어가 있다. funcs를 돌면서 f()를 포함하면 콜을 하게 되는데 이 때 n의 마지막 값이 three이기 때문에 three가 나온다.

**lambda Evaluation Time example - 2**
```python
numbers = 'one', 'two', 'three'
funcs = []
for n in numbers:
    funcs.append(lambda n=n: print(n))  # 그 때 그 때 parameters에 넣어서 저장시킨다.

for f in funcs:
    f()

''''''''''
one
two
three
''''''''''
```

### Appropriate Uses of Lambda Expressions

Python의 lambda는 아래와 같은 여러 논란들이 있다.

- Issues with readability(가독성 문제)
- The imposition of a functional way of thinking(기능적 사고방식 문제)
- Heavy syntax with the lambda keyword(lambda keyword를 사용한 무거운 문법)

**Classic Functional Constructs**
lambda function은 built-in 기능으로 map() and filter()를 사용할 수 있습니다. 추가로 functools.reduce()와 같이 functools module도 사용할 수 있다.

```python
list(map(lambda x: x.upper(), ['cat', 'dog', 'cow']))
['CAT', 'DOG', 'COW']

list(filter(lambda x: 'o' in x, ['cat', 'dog', 'cow']))
['dog', 'cow']

from functools import reduce
reduce(lambda acc, x: f'{acc} | {x}', ['cat', 'dog', 'cow'])
'cat | dog | cow'
```

**Key Functions**

sort, sorted 둘 다 Key parameter를 갖고 있고 정렬을 목적으로 하는 함수를 넣는다. 여기서는 lambda를 이용한다.

Key값을 기준으로 정렬되고 기본값은 오름차순(reverse=False)이다.

- sort(): list method
- sorted(), min(), max(): built-in functions
- nlargest() and nsmallest(): in the Heap queue algorithm module heapq

```python
ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
print(sorted(ids))
''''''''''
['id1', 'id100', 'id2', 'id22', 'id3', 'id30']
''''''''''

sorted_ids = sorted(ids, key=lambda x: int(x[2:]))
print(sorted_ids)
''''''''''
['id1', 'id2', 'id3', 'id22', 'id30', 'id100']
''''''''''

tuple_list = [
    ('B', 1),
    ('C', 8),
    ('E', 3),
    ('D', 4),
    ('A', 10),
]
tuple_list.sort(key=lambda x: (x[0]))
print(tuple_list)
''''''''''
[('A', 10), ('B', 1), ('C', 8), ('D', 4), ('E', 3)]
''''''''''

tuple_list.sort(key=lambda x: (x[1]))
print(tuple_list)
''''''''''
[('B', 1), ('E', 3), ('D', 4), ('C', 8), ('A', 10)]
''''''''''
```

## Reference
https://realpython.com/python-lambda/
decorator https://medium.com/@hckcksrl/python-%EB%8D%B0%EC%BD%94%EB%A0%88%EC%9D%B4%ED%84%B0-decorator-980fe8ca5276
closure http://schoolofweb.net/blog/posts/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%81%B4%EB%A1%9C%EC%A0%80-closure/
