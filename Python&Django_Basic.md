# Python

## 가변인자

```python
def print_num(*numbers):
    for number in numbers:
        print(number)

print_num(1,2,3,4)
```

* 가변인자 뒤에는 일반인자가 올 수 없으며 하나만 사용할 수 있습니다.
* 가변인자를 * 한 개만 사용하여 받으면 튜플 형태로 전달되고 두 개면 딕셔너리 형태로 받아옵니다.

```python
def print_num(*numbers, **name):
    for number in numbers:
        print(number)

    print("\n{0}".format(name))

print_num(1, 2, 3, 4, name="Bob", name2="julia")
```

## 퍼스트클래스 함수(First Class Function)

* 퍼스트클래스 함수란 프로그래밍 언어가 함수(function) 를 first_class citizen 으로 취급하는 것을 의미합니다.
쉽게 설명하자면 하뭇 자체를 인자(argument)로써 다른 함수에 전달하거나 다른 함수의 결과값으로 리턴 할수도 있고,
함수를 변수에 할당하거나 데이터 구조안에 저장할 수 있는 함수를 뜻 합니다.

* 프로그래밍 언어 디자인에서 프로그래밍 언어의 first-class citizen 은 다른 엔티티가 일반적으로 사용할 수 있는
모든 작업들을 지원하는 엔티티라고 합니다. 이러한 작업들에는 객체 등 함수의 인자로 넘기거나, 함수에서 반환하고 변수에 할당할 수 있는
것들이 포함되어 있습니다. 

일반적으로 1급 시민의 조건은 다음과 같이 정의한다고 합니다.
- 변수(variable)에 담을 수 있다.
- 인자(parameter)로 전달할 수 있다.
- 반환값(return value)으로 전달할 수 있다.

## 클로저
### 중첩함수(nested function)
- 함수 안에 함수를 정의한 것을 말합니다.
- 중첩함수를 통해 default 로 enclosing function local scope 변수를 참조할 수 있습니다.

### 내부 함수와 외부 함수
```python
def outer_func(msg):
    def inner_func():
        print(msg)
    
    return inner_func
```
- inner_func 을 내부함수, outer_func 를 외부함수라고 합니다.
- inner_func 입장에서 outer_func 함수의 지역변수 영역을 enclosing function local scope (바깥 함수 지역 변수 영역) 라고 부릅니다.

### 클로저(closure)란
```python
def outer_func(msg):
    def inner_func():
        print(msg)
    
    return inner_func

my_func = outer_func('Hello')
my_func()  # Hello
```
- 내부함수가 외부함수의 맥락(context)에 접근할 수 있는 것을 가리킵니다.
- inner_func 가 outer_func의 지역변수인 msg를 참조하여 출력하는 것을 볼 수 있습니다.
- 함수를 변수에 저장할 수 있는 이뉴는 파이썬에서는 함수가 **일급 객체(first-class object)** 이기 때문입니다.

```python
def outer_func(msg):
    def inner_func():
        print(msg)
    
    return inner_func

first_func = outer_func('First')  # first_func 객체(오브젝트) 생성
first_func()  # First

second_func = outer_func('Second')  # first_func 객체(오브젝트) 생성
second_func()  # second

print(id(outer_func))  # 4590816384
del outer_func

id(first_func())  # 4590521880
id(second_func())  # 4590532128
```
- outer_func 을 삭제해도 first_func 가 정상적으로 호출됩니다.
- 이는 함수를 변수에 저장할 때 마다 객체를 새롭게 생성하기 때문입니다. (모두 ID 값이 상이)

즉, first_func 와 second_func 는 서로 완전히 독립된 객체인 것 입니다.

### 클로저 내에서 enclosing function local scope 변수 Read/Write

- 클로저에서 enclosing local scope 변수에 접근할 수 있다면 modify 하는 것도 가능하지 않을까라고 생각할 수 있습니다.

```python
def outer_func(msg):
    def inner_func():
        print(msg)
        msg = "Awssss"
        print(msg)

    return inner_func

first_func = outer_func("Hello")
first_func()


UnboundLocalError: local variable 'msg' referenced before assignment
```
[!] 오류가 발생합니다.

- 첫 번쨰 print 문에서 inner_func 함수 내에서 msg 라는 변수는 선언된 적이 없기 때문에 enclosing function local scope에서 찾게 됩니다.
- 하지만 이 변수는 전역 변수와 마찬가지로 함수 내에서 수정할 수 없습니다. (파이썬 네임스페이스 참고) 
- 그래서 python 3.x 부터는 nonlocal 이라는 키워드를 통해 외부함수 영역의 변수를 modify할 수 있도록 합니다.(nonlocal은 global과 비슷한 개념)
- global / nonlocal -> 지역변수를 전역변수에 영향을 줄 수 있도록 해주는 명령어, global 명령어는 사용하지 않는 것을 권

#### 여기서 잠깐 global 과 nonlocal 에 대해 알아보자

> #### global
>
```python
x = 15  # 전역변수 (global variable)

def f():
    x = 30  # 지역변수 (local variable)

f()

print(x)
```
- 전역변수의 값 15가 출력되었다. 지역변수는 전역변수의 값에 영향을 끼칠 수 없다.
- 파이썬은 Call By Assignment

```python
x = 15  # 전역변수 (global variable)

def f():
    global x  # 함수의 지역변수 x 가 전역변수 x를 가리키게 된다.
    x = 30  # 지역변수 (local variable)

f()

print(x)
```
- x의 값은 30으로 변경되었다.

[!] 즉, mutable(변하는) 자료형을 가진 변수가 아닌 이상 지역변수가 전역변수에 영향을 줄 수 없다. 하지만 global 명령어를 사용할 경우 지역변수가 전역변수에 영향을 줄 수 있다.

> #### nonlocal
- 지역변수가 아님을 선언, nonlocal 이 사용된 함수 바로 한단계 바깥쪽에 위치한 변수와 바인딩을 할 수 있다.

```python
x = 20  # 전역변수 (global variable)

def f():
    x = 40  # 지역변수 (local variable)
    
    def g():
        nonlocal x
        x = 80
    g()
    print(x)  # 80

f()
print(x)  # 20
```
- 위 코드를 통해 알 수 있듯이, 바로 위에 해당하는 f 함수의 지역변수에만 영향을 주고, 전역 변수에는 영향을 주지 않는다.

[!] 함수 한 개를 정의하고 전역변수에 영향을 주게하는 것은 안된다. 무조건 중첩함수(Nested function)만 가능하다.

# 오브젝트란?
## 객체지향(OOP) 프로그램
* 프로그래밍으로 문제해결을 더 쉽게 하기 위해
* 큰 프로그램의 유지보수를 편하게 하기 위해
* 막장을 미연에 방지하기 위해 사용하는 개발 방법론이다.

## 오브젝트 = 객체
* Object is thing
* 실생활에 존재하는 어떤 것
* 상태와 행동을 가짐


## 클래스
* 오브젝트를 생성하기 위한 틀(템플릿)
* 상태(state)와 행동(behavior)를 가짐
* 객체는 클래스의 인스턴스다.

## Django 와 Object
* Django 는 많은 부분에 객체를 활용한다.
* Models
* CBV(Class-Based View)
* MTV(Model - Template - View)

## 요약
* 클래스: 메서드와 값을 가지는 사용자 정의 데이터 타입
* 객체(오브젝트): 클래스를 인스턴스화 한 것
* 객체 == 오브젝트 == instance 모두 비슷한 맥락에서 사



## Reference 

- https://ncookie.tistory.com/34
- https://ncookie.tistory.com/40?category=909804