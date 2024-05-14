# 3.2 지능형 딕셔너리
## 지능형 리스트와 제너레이터 표현식 구문이 지능형 딕셔너리에도 적용된다. (지능형 집합도 마찬가지다.)
## 지능형 딕셔너리는 모든 반복형 객체에서 키-값 쌍을 생성함으로써 딕셔너리 객체를 만들 수 있다.
# BEGIN DIALCODES
# dial codes of the top 10 most populous countries
DIAL_CODES = [
        (86, 'China'),
        (91, 'India'),
        (1, 'United States'),
        (62, 'Indonesia'),
        (55, 'Brazil'),
        (92, 'Pakistan'),
        (880, 'Bangladesh'),
        (234, 'Nigeria'),
        (7, 'Russia'),
        (81, 'Japan'),
    ]

country_code = {country: code for code, country in DIAL_CODES}  # {'China': 86, ... }
"""
{'China': 86,
    'India': 91,
    'United States': 1,
    'Indonesia': 62,
    'Brazil': 55,
    'Pakistan': 92,
    'Bangladesh': 880,
    'Nigeria': 234,
    'Russia': 7,
    'Japan': 81
    }
"""
# target = dict(sorted(country_code.items(), key=lambda x: x[1]))  # code 오름차순 후 dict 
target = {code: country.upper() for country, code in country_code.items() if code < 66}
# {1: 'United States', 62: 'Indonesia', 55: 'Brazil', 7: 'Russia'}

d1 = dict(DIAL_CODES)  # <1>
print('d1:', d1.keys())
d2 = dict(sorted(DIAL_CODES))  # <2>
print('d2:', d2.keys())
d3 = dict(sorted(DIAL_CODES, key=lambda x:x[1]))  # <3>
print('d3:', d3.keys())
assert d1 == d2 and d2 == d3  # <4>
# END DIALCODES
"""
# BEGIN DIALCODES_OUTPUT
d1: dict_keys([880, 1, 86, 55, 7, 234, 91, 92, 62, 81])
d2: dict_keys([880, 1, 91, 86, 81, 55, 234, 7, 92, 62])
d3: dict_keys([880, 81, 1, 86, 55, 7, 234, 91, 92, 62])
# END DIALCODES_OUTPUT
"""

