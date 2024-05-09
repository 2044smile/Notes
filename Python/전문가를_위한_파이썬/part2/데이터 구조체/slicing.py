# 파이썬에서 제공하는 list, tuple, str, 그리고 모든 시퀀스형은 슬라이싱 연산을 지원한다.
# 고급 슬라이싱 형태의 사용법을 설명한다.

## 2.4.1 슬라이스와 범위 지정시에 마지막 항목이 포함되지 않는 이유

l = [10, 20, 30, 40, 50, 60]
l[:2]  # [10, 20]
l[2:]  # [30, 40, 50, 60]
l[:3]  # [10, 20, 30]
l[3:]  # [40, 50, 60]

## 2.4.2 슬라이스 객체
### slice(a, b, c) 객체를 생성한다.
### stride 보복 [::`it`]
### 파이썬은 s.__getitem__(slice(start, stop, step)) 을 호출한다.
s = 'bicycle'
s[::3]  # '`b`ic`y`cl`e`' -> bye
s[::-1]  # elcycib
s[::-2]  # eccb

## 2.4.3 다차원 슬라이싱과 생략 기호
### [] 연산자는 콤마로 구분해서 여러 개의 인덱스나 슬라이스를 가질 수 있다.
### [] 연산자는 __getitem__(), __setitem__() 특수 메서드는 a[i, j] 에 들어 있는 인덱스들을 튜플로 받는다.
### 파이썬에 내장된 시퀀스형은 1차원이므로 단 하나의 인덱스나 슬라이스만 지원하고, 튜플은 지원하지 않는다.

# my
lst = [1,2,3]
lst.__getitem__(0)  # 1
lst.__setitem__(-1, 99)  # [1, 2, 99]
lst.__iadd__([999])  # [1, 2, 99, 999]
lst.append(9999)  # [1, 2, 99, 999, 9999]

## 2.4.4 슬라이스에 할당하기
### 할당문의 왼쪽에 슬라이스 표기법을 사용하거나 del 문의 대상 객체로 지정함으로써
### 가변 시퀀스를 연결하거나, 잘라 내거나, 값을 변경할 수 있다.

lst = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lst[2:5] = [20, 30]  # [0, 1, 20, 30, 5, 6, 7, 8, 9] -> del [4]
del lst[5:7]  # [0, 1, 20, 30, 5, 8, 9]
lst[3::2] = [11, 22]  # [0, 1, 20, `30`, 5, `8`, 9] -> [0, 1, 20, 11, 5, 22, 9]
# lst[2:5] = `100`  # TypeError: can only assign an iterable
## 반복 가능한 객체가 와야 한다.
lst[2:5] = [100]  # [0, 1, 100, 22, 9]

## 2.5 시퀀스에 덧셈과 곱셈 연산자 사용하기
### 파이썬은 시퀀스가 당연히 덧셈과 곱셈을 지원한다고 알고 있다.
### 일반적으로 덧셈의 경우 피연산자 두 개가 같은 자료형이어야 하며, 둘 다 변경되지 않지만 동일한 자료형의 시퀀스가 새로 만들어진다.
lst = [1, 2, 3]
lst * 5  # [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3] 시퀀스 생성, 객체 생성
print(lst)  # [1, 2, 3]
