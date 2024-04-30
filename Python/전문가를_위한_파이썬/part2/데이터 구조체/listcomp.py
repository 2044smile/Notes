# v1
symbols = '$%^&*'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
# [36, ...]

# v2; 지능형 리스트
symbols = '$%^&*'
codes = [ord(symbol) for symbol in symbols]  # 지능형 리스트
codes
# [36, ...]

# map()/filter() 비교
symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
beyond_ascii
# [..., ...]

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
beyond_ascii

# 데카르트 곱
# 지능형 리스트는 두 개 이상의 반복 가능한 자료형의 데카르트 곱을 나타내는 일련의 리스트를 만들 수 있다.
# 2-4. 지능형 리스트를 이용한 데카르트 곱
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
# [('black', 'S'), ('black', 'M'), ('black', 'L'),
#  ('white', 'S'), ('white', 'M'), ('white', 'L')]

for color in colors:
    for size in sizes:
        print((color, size))

# ('black', 'S')
# ('black', 'M')
# ...
# ('white', 'L)

tshirts = [(color, size) for size in sizes for color in colors]
tshirts
# [('black', 'S'), ('white', 'S'), ('black', 'M') ...]

# 제너레이터 표현식
# 튜플, 배열 등의 시퀀스형을 초기화하려면 지능형 리스트를 사용할 수도 있지만
# 다른 생성자에 전달할 리스트를 통째로 만들지 않고 반복자 프로토콜을 이용해서 
# `항목을 하나씩 생성하는 제너레이터 표현식은 메모리를 더 적게 차지한다.`

# 2-5. 제너레이터 표현식에서 튜플과 배열 초기화하기
symbols = '$¢£¥€¤'
tuple(ord(symbol) for symbol in symbols)
# (36, 162, 163, 165, 8364, 164)
import array
array.array('I', (ord(symbol) for symbol in symbols))
# array('I', [36, 162, 163, 165, 8364, 164])

# 2-6. 제너레이터 표현식에서의 데카르트 곱
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)
# 여기서는 단지 리스트 이외의 시퀀스를 초기화하거나,
# 메모리에 유지할 필요가 없는 데이터를 생성하기 위해
# 제너레이터 표현식을 사용하는 방법만 보여주었다.

# 튜플은 단순한 불변 리스트가 아니다.
# 튜플은 불변 리스트로 사용할 수도 있지만 필드명이 없는 레코드로 사용할 수도 있다.

# 2-7. 레코드로 사용된 튜플
lax_coordinates = (33.9425 - 118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '311'), ('BRA', 'CE3'), ('ESP', 'XDA')]

for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)

# divmod
divmod(20, 8)
# (20 // 8, 20 % 8)
# (2, 4)
t = divmod(20, 8)  # (2, 4) 호출 될 때 마다
divmod(*t)

quotient, remainder = divmod(*t) # 몫, 나머지 [언패킹] | (0, 2)
print(quotient, remainder)

# 함수에서 호출자에 여러 값을 간단히 반환하는 기능이다.
import os
_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
filename  # 'idrsa.pub'

# 초과 항목을 잡기 위해 * 사용하기
a, b, *rest = range(5)
# a, b, rest
# (0, 1, [2, 3, 4])

a, b, *rest = range(3)
# (0, 1, [2])

a, b, *rest = range(2)
# (0, 1, [])

a, *body, c, d = range(5)
# (0, [1,2], 3, 4)
*head, b, c, d = range(5)
# ([0, 1], 2, 3, 4)

# 내포된 튜플 언패킹
# longitude에 접근하기 위해 내포된 튜플 언패킹하기
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),   # <1>
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))  # {:^9} 문자열이 중앙에 위치하도록
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:  # <2>
    if longitude <= 0:  # <3>
        print(fmt.format(name, latitude, longitude))

