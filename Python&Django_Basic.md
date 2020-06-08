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