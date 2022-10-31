# 확인 문제

## 다음 빈칸을 채워서 numbers 내부에 들어 있는 숫자가 몇 번 등장하는지를 출력하는 코드를 작성해 보세요.
```python
# 문제1
# 숫자는 무작위로 입력해도 상관 없습니다.
numbers = [1,2,6,3,4,5,7,2,1,5,7,9,5,3,2,6,8]
counter = {}

# (1) 요소의 출현을 확인하는 코드
for number in numbers:
    if number not in counter:
        counter[number] = 0
    counter[number] += 1

print(counter)

# 문제2
character = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
    },
    "skill": ["베기", "세게 베기", "아주 세게 베기"]
}

for key in character:
    if type(character[key]) is dict:
        for ke in character[key]:
            print(f"{ke} : {character[key][ke]}")
    elif type(character[key]) is list:
        for k in character[key]:
            print(f"skill : {k}")
    else:
        print(f"{key} : {character[key]}")

# name : 기사
# level : 12
# sword : 불꽃의 검
# armor : 풀플레이트
# skill : 베기
# skill : 세게 베기
# skill : 아주 세게 베기
```