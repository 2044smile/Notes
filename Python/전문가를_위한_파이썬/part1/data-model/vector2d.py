from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # def __str__(self): interface 로서의 역할을 수행하기 위해 존재합니다.
    # 서로 다른 타입을 가진 데이터끼리 상호작용 할 때 문자열로 변환시킴으로서 상호간의 호환
    # 참고로 print 는 내부적으로 str 메소드를 호출합니다.

    def __repr__(self):  # 객체를 문자열로 반환 즉 객체가 어떤 타입을 가졌던 간에 그것을 문자열로서 반환
        # eval(expression) 함수에 사용 가능, 새로운 객체를 만들어 내는 것도 가능
        # 참고로 __str__ 메소드의 반환 값은 eval 함수에 사용할 수 없다.
        # eval("1 + 2") 문자열이 매개변수로 들어오면 3이라는 값을 출발
        # 즉, "문자열로 식을 입력"하면 "해당 식을 실행한 결과 값"을 반환해주는 그런 함수
        # return Vector(%r, %r)' % (self.x, self.y)
        return f"Vector({self.x}, {self.y})"

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):  # other 에는 다른 인스턴스
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


v1 = Vector(x=5, y=5)
v2 = Vector(x=10, y=10)
obj = v1 + v2  # __add__ 실행
print(obj)

# 특별 메서드를 구현하면 __something__ 사용자 정의 객체도 내장형 객체처럼 작동하게 되어,
# 파이썬스러운 표현력 있는 코딩 스타일을 구사할 수 있다.
# 디버깅 and 로깅에 사용 __repr__()
# 사용자에게 보여주는 __str__()
