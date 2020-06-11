# 데코레이터(Decorator)

## 개념
- 데코레이터란 사전적 의미로는 "장식가" 또는 "인테리어 디자이너" 등의 의미를 가지고 있습니다. 이름 그대로,
자신의 방을 예쁜 벽지나 커트느올 장식을 하듯이, 기존의 코드에 여러가지 기능을 추가하는 파이썬 구문이라고 생각하시면 됩니다. 많은 파이썬 초보자들이 데코레이터를 이해하는 어려움을겼습니다. 그런데 데코레이터란 그렇게 어려운 개념이 아닙니다.

## 실습
```python
def outer_func(msg):
    def inner_func():
        print(msg)
    return inner_func

hi_func = outer_func('Hi')
bye_func = outer_func('Bye')

hi_func()  # Hi
bye_func()  # Bye
```

- 데코레이터 코드도 위의 코드와 아주 비슷합니다. 다만 함수를 다른 함수의 인자로 전달한다는 점이 조금 틀립니다.

```python
def decorator_func(original_func):  #1
    def wrapper_func():  #5
        return original_func()  #7
    return wrapper_func  #6

def display():  #2
    print('display run')  #8

decorated_display = decorator_func(display)  #3

decorated_display()  #4
```

데코레이터 함수인 decorator_func 와 일반 함수인 display를 #1과 #2에서 각각 정의하였습니다.
그 다음에 #3에서 decorated_display라는 변수에 display 함수를 인자로 갖은 decorator_func을 실행한 리턴값을 할당하였습니다.
물론 이 리턴 값은 wrapper_func가 되겠죠. 여기서 wrapper_func 함수는 아직 실행된게 아닙니다. decorated_display 변수 안에서 호출되기를 기다리는 겁니다. 그리고 #4의
decorated_display()를 통해 wrapper_func를 호출하면 #5번에서 정의된 wrapper_func이 호출이 됩니다.
그러면 #7에서 original_func인 display 함수가 호출되어 #8의 print 함수가 호출되고 문자열이 출력되는 겁니다.

- 데코레이터를 사용하는 이유는 이미 만들어져 있는 기존의 코드를 수정하지 안혹도, 래퍼(wrapper) 함수를 이용하여 여러가지 기능을 추가할 수 있기 떄문입니다.

```python
def decorator_func(get_func):
    def wrapper_func(*args, **kwargs):
        print('{} 함수가 호출되기 전 입니다.'.format(get_func))
        return get_func(*args, **kwargs)
    return wrapper_func()

@decorator_func
def display():
    print('run display')

@decorator_func
def display_info():
    print('display_info({}, {}) 함수가 실행됐습니다.'.format(name, age))

display()  
# display 함수가 호출되기 전 입니다.
# run display
display_info('lee', 25)
# display_info 함수가 호출되기 전 입니다.
# display_info(lee, 25) 함수가 실행됐습니다.
```

- @decorator_func 는 decorator_func 함수의 인자로 어떤 함수를 넘길지를 의미합니다. 바로 아래있는 display 인자로 넘어갑니다.
- 자연스럽게 이중함수 구조이기 때문에 안에 있는 wrapper_func로 인자가 있다면 전달되고, 없다면 전달되지 않고 '함수가 호출되기 전 입니다' 라는 메시지를 띄웁니다.
- 그리고 get_func 를 호출하게 됩니다.

데코레이터는 이런 함수 형식 마록도 클래스 형식을 사용할 수도 있습니다.

```python
class DecoratorClass:  #1
    def __init__(self, original_function):
        self.original_function = original_function
        print('__init__')

    def __call__(self, *args, **kwargs):
        print('{} 함수가 호출되기전 입니다.'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@DecoratorClass  #2
def display():
    print('display 함수가 실행됐습니다.')


@DecoratorClass  #3
def display_info(name, age):
    print('display_info({}, {}) 함수가 실행됐습니다.'.format(name, age))

display()
print
display_info('John', 25)
```

- __init__이란 생성자입니다. 해당 클래스가 호출될 때 실행되고, print 를 찍어놓았으니 __init__이 출력되는 것을 확인할 수 있습니다.
- __call__ 호출할 때 실행됩니다. 아까와 결과는 똑같습니다.
- 클래스 데코레이터는 그다지 많이 사용되지 않고, 보통 함수 형식이 많이 사용됩니다.


일반적으로 데코레이터는 로그를 남기거나 유저의 로그인 상태 등을 확인하여 로그인 상태가 아니면 로그인 페이지로 리다이렉트 하기 위해서 많이 사용됩니다.
또한 프로그램의 성능을 테스트하기 위해서도 많이 쓰입니다.

데코레이터를 이용하여 로깅 기능을 만들어보겠습니다.

```python
import datetime
import time


def my_logger(original_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strtime('%Y-%m-%d %H:%M')
        logging.info(msg='실행결과')
        return original_func(*args, **kwargs)

    return wrapper


@my_logger
def display_info(name, age):
    time.sleep(1)
    print('display_info({}, {}) 함수가 실행됐습니다.'.format(name, age))


display_info('cslee', 25)

```

- 만들면서 느낀 점은 logger에서 파일생성 해주는 것을 지원해주는데 굳이..? 라는 생각이 들었습니다.
- 위에 실전 예시에서 로그인 안한 유저를 확인할 때는 정말 도움 될 듯 합니다.

## Reference
- http://schoolofweb.net/blog/posts/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%8D%B0%EC%BD%94%EB%A0%88%EC%9D%B4%ED%84%B0-decorator/