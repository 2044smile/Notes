# 리스트와 반복문

1. 수학의 수열

```pythono
"가나다라"  # 문자들이 일렬로 나열된 것: 문자열
1 2 3 4  # 숫자들이 일렬로 나열된 것: 수열

a = (1,2,3,4)
# 항: 수열의 요소
# 1번 째 항: 1
# 2번 째 항: 2
# 3번 째 항: 3
# 4번 째 항: 4

# 길이: 수열 요소의 수 -> 4
## 유한 수열: 길이가 유한한 수열
## 무한 수열: 길이가 무한한 수열

# 수학의 수열은 a1, a2, a3처럼 1부터 세지만
# 프로그래밍의 배열은 (대부분) a[0], a[1], a[2]처럼 0부터 셉니다.

# 서수와 기수
## 서수: 순서를 나타내는 숫자 first, second, third...
## 기수: 개수를 나타내는 숫자 one, two, three...
```

2. 프로그래밍의 배열
3. 프로그래밍의 배열과 리스트
   1. 배열: 길이가 고정
   2. 리스트: 배열에 요소 추가 제거 등의 기능을 추가한 것
4. 간단하게 리스트 사용해보기
   1. 리스트 반대로 돌리기
      1. a = [start:end:step]
         1. "abcde"[::-1]
   2. 중첩 리스트
      1. b = [['a', 'a', 'a'], ['b', 'b'], ['c', 'c']]
      2. b[0] # ['a','a','a']
      3. b[0][0] # 'a'