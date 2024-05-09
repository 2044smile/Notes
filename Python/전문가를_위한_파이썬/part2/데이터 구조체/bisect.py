# 2.8 정렬된 시퀀스를 bisect로 관리하기
## bisect 모듈은 bisect() 와 insort() 함수를 제공한다.
### bisect() 는 이진 검색 알고리즘을 이용해서 시퀀스를 검색
### insort() 는 정렬된 시퀀스 안에 항목을 삽입한다.

# 2.8.1 bisect() 로 검색하기
## bisect(haystack, needle) 은 정렬된 시퀀스인 haystack 안에서 오름차순 정렬 상태를 유지한 채로 needle을 추가할 수 있는 위치를 찾아낸다.
## 즉, 해당 위치 앞에는 needle 보다 같거나 작은 항목이 온다.
## `이진탐색이란, 정렬되어 있는 리스트 안에서 특정 값을 찾아내는 것이다.`
from bisect import bisect_left, bisect_right

# [left_v, right_v] 범위 내에 있는 원소 개수 출력 함수
def cnt_within_range (arr, left_v, right_v):
    # 맨 좌측 인덱스
    left_idx = bisect_left(arr, left_v)
    print(left_idx)
    # 맨 우측 인덱스 + 1 되는 듯?
    right_idx = bisect_right(arr, right_v)
    print(right_idx)
    return right_idx - left_idx

# 리스트 생성
arr = [5, 6, 7, 7, 7, 7, 8, 8, 9, 10]

# 값이 9인 `원소 개수 출력` == lst.count(7)
print(cnt_within_range(arr, 9, 9)) # 1
# [4, 7] 범위 내에 있는 `원소 개수 출력`
print(cnt_within_range(arr, 4, 7)) # 6
# ---
import bisect

lst = [1,3,4,5]
# bisect(): `오름차순`으로 정렬된 시퀀스에 x 값이 들어갈 위치 리턴
bisect.bisect(lst, 2)
# bisect_right(): x와 동일한 값이 시퀀스 a에 존재할 때 x와 동일한 값 바로 뒤 위치를 리턴
bisect.bisect_right(lst, 3)
# bisect_left(): x와 동일한 값이 시퀀스 a에 존재할 때 동일한 값 위치를 리턴, 
# 리스트에 찾는 값의 원소가 존재하지 않는 경우 정렬 순서상 해당 값을 삽입해야 할 자리의 인덱스 리턴
bisect.bisect_left(lst, 3)
# ***
# 정리
lst = [1, 1, 1, 4, 5, 6]
bisect.bisect_left(lst, 6)  # 왼쪽 -> 오른쪽으로 6이 위치할 위치를 찾는다. -> [1, 1, 1, 4, 5, ``, 6] -> `` 인덱스 5 를 리턴한다.
bisect.bisect_right(lst, 6)  # 오른쪽 -> 왼쪽 6이 위치할 위치를 찾는다. -> [1, 1, 1, 4, 5, 6, ``] -> `` 인덱스 6를 리턴한다.
## bisect_left, right() 
# ***
# 2.8.2 bisect.insort() 로 삽입하기
lst = [1, 1, 1, 4, 5, 6]

bisect.insort(lst, 2)  # [1, 1, 1, 2, 4, 5, 6]
