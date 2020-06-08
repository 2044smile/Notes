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

## Reference
- http://schoolofweb.net/blog/posts/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%8D%B0%EC%BD%94%EB%A0%88%EC%9D%B4%ED%84%B0-decorator/