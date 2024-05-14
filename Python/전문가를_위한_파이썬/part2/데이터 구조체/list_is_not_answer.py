# 2.9 리스트가 답이 아닐 때
## 리스트형(list)은 융통성 있고 사용하기 편하지만, 세부 요구사항에 따라 더 나은 자료형도 있다.
## 예를 들어 실수를 `천만 개 저장해야 할 때는 배열(array)이 훨씬 더 효율적`이다.
## `배열은 모든 기능을 갖춘 float 객체 대신 C언어의 배열과 마찬가지로 기계가 사용하는 형태로 표현된 바이트 값만 저장하기 때문이다.`
## `한편 리스트의 양쪽 끝에 항목을 계속 추가하거나 삭제하면서 FIFO나 LIFO 데이터 구조를 구현할 때는 덱(deque; 양쪽을 사용하는 큐)가 더 빠르다.`
## set(튜플) 형은 항목이 들어 있는지 검사하는 과정이 최적화되어 있다.

# 2.9.1 배열
## 리스트 안에 `숫자만 들어 있다면 배열(array.array)이 리스트보다 훨씬 더 효율적`이다.
## 배열은 pop(), insert(), extend() 등을 포함해서 가변 시퀀스가 제공하는 모든 연산을 지원하며, 
## 빠르게 파일에 저장하고 읽어올 수 있는  frombytes()와 tofile() 메서드도 추가로 제공한다.
## 파이썬 배열은 C 배열 만큼 가볍다. / C기반 형을 결정하는 문자일 타입코드(typecode)를 지정한다.

## 2-20 커다란 실수 배열의 생성, 저장, 로딩
### 숫자의 경우 배열 사용
### 객체를 바이트로 변환하는 이유는 주로 데이터를 저장하거나 전송하기 위함이다.
### 바이트로 변환된 데이터는 메모리나 디스크에 저장할 수 있고, 네트워크를 통해 전송할 수도 있다.
### `바이트 형식은 텍스트보다 효율적이고 속도가 빠르며, 데이터의 유형에 관계없이 일관된 방식으로 처리`될 수 있다.
### 객체를 바이트로 변환하는 것은 데이터의 저장, 전송, 공유를 용이하게 하고,
### 객체를 다양한 환경에서 사용할 수 있도록 하는 중요한 과정이다.
from array import array
from random import random


floats = array('d', (random() for i in range(10**7)))  # 배열 생성
print(floats[-1])

fp = open('floats.bin', 'wb')
floats.tofile(fp)  # 생성 된 배열 floats.bin 에 저장
floats.close()

floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)  # 로딩
fp.close()
print(floats2[-1])

print(floats == floats2)  # True

# 2.9.2 메모리 뷰
## 메모리 뷰(memoryview) 내장 클래스는 공유 메모리 시퀀스형으로서 bytes 를 복사하지 않고,
## 시퀀스란 문자열, 리스트, 튜플 등의 인덱스를 가지는 자료형
## 배열의 슬라이스를 다룰 수 있게 해준다.
## memoryview 객체를 사용하여 바이트 데이터를 가져와 특정 위치에서의 데이터를 추출하거나 데이터를 수정할 수 있다.
## memoryview 객체를 사용하면, 바이트객체와 같은 메모리 위치에서의 데이터를 직접 접근할 수 있으므로, `연산 속도가 높아지고 메모리 사용량이 줄어드는 효과를 볼 수 있다.`
## 1. 바이트 배열을 공유하는 경우: memoryview 객체를 사용하면 동일한 바이트 배열의 복사본을 만들 필요 없이 바이트 데이터를 공유할 수 있다.
## 2. 바이트 데이터를 효율적으로 처리하는 경우: memoryview 객체는 파이썬의 내장 메모리 관리 기술을 이용해 바이트 데이터를 효율적으로 처리할 수 있다.
## 메모리뷰를 사용하면 데이터를 복사할 필요 없이, 데이터에 직접 접근할 수 있어 처리 속도가 향상된다.
## 3. 바이트 데이터에 대한 작업을 수행하는 경우: memoryview 객체를 사용하면 바이트 데이터에 대한 여러 종류의 작업을 수행할 수 있다. 
## 예를 들어, 바이트 데이터의 특정 부분을 슬라이싱하거나, 바이트 데이터의 특정 위치에서 특정 타입의 값을 읽을 수 있다.
## 바이트 객체
### 바이트 객체는 말 그대로 데이터 형식이 바이트 단위로 구성된 객체를 의미
### e.g) b = bytes([0x41, 0x42, 0x43])
### 바이트 객체를 사용하면 이점은 아래와 같다.
#### 1. 표준화: 바이트 형식은 컴퓨터에서 구조화된 데이터를 표준화하는 데 많이 사용된다.
#### 따라서, 바이트 형식으로 저장된 데이터는 다양한 플랫폼에서 쉽게 공유 및 처리할 수 있다.
#### 2. 효율성: 바이트 형식으로 데이터를 저장하면, 데이터 크기를 줄일 수 있으며, 처리 속도도 빠르다.
#### 3. 간결성: 바이트 형식으로 데이터를 저장하면, 데이터를 저장하는데 필요한 저장 공간이 줄어들고, 데이터 전송 또한 빠르게 이루어진다.

## 2-21 배열 항목 값의 바이트 중 하나를 변경하기
### array 모듈과 비슷한 표기법을 사용하는 memoryview.cast() 메서드는 바이트를 이동시키지 않고 C언어의 형변환 연산자처럼 여러 바이트로 된 데이터를 읽거나 쓰는 방식을 바꿀 수 있게 해주고 
### memoryview.cast()는 또 다른 memoryview 객체를 반환하며 언제나 동일한 메모리를 공유한다.
### https://velog.io/@qsdcfd/%EB%A6%AC%EC%8A%A4%ED%8A%B8%EA%B0%80-%EB%8B%B5%EC%9D%B4-%EC%95%84%EB%8B%90-%EB%95%8C
import array


numbers = array.array('h', [-2, -1, 0, 1, 2])  # 'h' = int(짧은 정수)
memv = memoryview(numbers)  # numbers 를 가지고 memoryview 생성
len(memv)  # 5 -> 값 보존
print(memv[0])  # -2 -> 값 보존
memv_oct = memv.cast('B')  # 'B' = char 형 변환
memv_oct.tolist()  # [254, 255, 255, 255, 0, 0, 1, 0, 2, 0]
memv_oct[5] = 4
print(numbers)  # array('h', [-2, -1, 1024, 1, 2]) 1024

# 2.9.4 덱 및 기타 큐
## 리스트를 스택이나 큐(append() and pop() 을 사용하면 FIFO 방식으로 작동한다.)
##* 덱(collections.deque) 클래스는 큐의 양쪽 어디에서든 빠르게 삽입 및 삭제할 수 있도록 설계된 스레드 안전한 양방향 큐다
##* 단점 덱의 중간 항목을 삭제하는 연산은 그리 빠르지 않다. 덱이 양쪽 끝에 추가나 제거하는 연산에 최적화 되어 있기 때문이다.
from collections import deque


dp = deque(range(10), maxlen=10)
print(dp)  # deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
dp.rotate(3)  # deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], maxlen=10) 
dp.rotate(-4) # deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], maxlen=10)
# rotate() 메서든는 양수 인수를 받으면 오른쪽 끝에 있는 항목을 지정한 개수만큼 왼쪽(오른쪽으로 이동) 끝으로, 
# 음수 인수를 받으면 왼쪽 끝에 있는 항목을 지정한 개수만큼 오른쪽(왼쪽으로 이동) 끝으로 이동한다.
#* 결론 양수(3) 은 전체가 3칸 오른쪽으로 이동, 음수(3) 은 전체가 3칸 왼쪽으로 이동
dp.appendleft(999)  # deque([999, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
#* maxlen 을 10으로 유지 했기 떄문에 리스트 맨 마지막 값 제거
dp.extend([11, 22, 33])  # 추가 왼쪽 999, 0, 1 삭제
# deque([2, 3, 4, 5, 6, 7, 8, 11, 22, 33], maxlen=10)
dp.extendleft([11, 22, 33])  # deque([33, 22, 11, 2, 3, 4, 5, 6, 7, 8], maxlen=10)

#* 표준 라이브러리 설명
## queue
### queue 모듈에서는 동기화된 (즉, 스레드 안전한) Queue, LifoQueue, PriorityQueue 클래스를 제공한다.
### 이 클래스들은 스레드 간에 안전하게 통신하기 위해 사용된다.
### 세 클래스 모두 0보다 큰 maxsize 인수를 생성자에 전달해서 바인딩 할 수 있다.
###* 그렇지만 덱(deque) 와 달리 공간이 꽉 찼을 때 항목을 버리지 않는다.
###* 대신 새로운 항목의 추가를 블로킹하고, 다른 스레드에서 큐 안의 항목을 제거해서 공간을 확보해줄 때 까지 기다린다.
###* 따라서, 활성화 된 스레드 수를 활성화 하기 좋다.

## multiprocessing
### 멀티프레소싱 모듈은 queue.Queue 와 비슷하지만 프로세스 간 통신을 지원하기 위해 설계된 고유한 Queue 클래스를 구현한다.
### 태스크 관리에 특화된 multiprocessing.JoinableQueue 클래스도 제공한다.

## asyncio
### queue 및 multiprocessing 모듈에 포함된 클래스로 부터 영감을 얻은 Queue, LifoQueue, PriorityQueue, JoinableQueue 클래스를 제공하지만,
###* `비동기 프로그래밍` 환경에서 작업을 관리하는 데 주안점을 두고 있다.

## heapq
### queue 클래스를 구현하지는 않지만, 가변 시퀀스를 힙 큐나 우선순위 큐로 사용할 수 있게 해주는 heappush() and heappop() 등의 함수를 제공한다.

# 2.10 요약
## 라이브러리에서 제공하는 시퀀스형을 제대로 파악하고 있어야 간결하고, 효율적이며, 파이썬스러운 코드를 작성할 수 있다.
## 파이썬 시퀀스는 가변형과 불변형으로 구분하기도 하지만, 균일 시퀀스와 컨테이너 시퀀스로 분류하는 것도 도움이 된다.
##* 컨테이너 시퀀스
### 서로 다른 자료형을 담을 수 있으며 list, tuple, collection.deque 형이 이에 속한다.
##* 균일 시퀀스
### 단 하나의 자료형만 담을 수 있으며 str, bytes, bytearray, memoryview, array.array 형이 이에 속한다.
##* 가변 시퀀스
### list, bytearray, array.array, collections.deque, memoryview 형이 이에 속한다.
##* 불변 시퀀스
### tuple, str, bytes형이 이에 속한다.
##* 지능형 리스트
### 리스트 구성을 위해 항목을 하나하나 나열하는 방식 외에 구문을 통해 sequence 형태의 데이터를 가공하여 리스트를 구성하는 방법을 제공
### 코드가 간결해지고, 상황에 따라서는 성능이 좋은 코드를 작성할 수 있다.
##* 제너레이터 표현식
### 지능형 리스트와 유사하지만 별도의 리스트는 생성하지 않고, iterator 를 생성하여 항목을 하나씩 처리할 수 있도록 한다.
### 지능형 리스트는 별도의 항목을 보유 즉, 메모리 공간을 차지 하지만 제너레이터 표현식은 별도의 메모리 공간을 차지하지 않는다. 
###* 지능형 리스트의 경우 대괄호 [] 를 사용하는 반면, 제너레이터 표현식은 괄호 () 를 사용하고,
### 나머지 구문은 동일하다. 변수로 저장해 놓고 리스트 형태로 써야 하는 경우는 지능형 리스트의 형태로 사용하면 되고, 메모리에 유지할 필요가 없을 경우 제너레이터 표현식의 형태로 사용하면 된다.

## 튜플
### 익명 필드를 가진 레코드 및 불변 리스트로 사용할 수 있다.
### 튜플을 레코드로 사용할 때는 튜플 언패킹이 필드에 접근하는 가장 안전하고 가독성이 좋은 방법이다.

## +=, *= 복합 할당 연산자
### 가변/불변 시퀀스 여부에 따라 다르게 작동한다.
### 복합 할당 연산자는 대상 시퀀스가 불변인 경우에는 새로운 시퀀스를 생성한다.
### 그러나, 대상이 가변인 경우에는 대상 시퀀스를 직접 변경한다.

## sort(): 메서드, sorted(key, reverse): 내장함수
### sorted 는선택적인 key 인수에 정렬 기준 계산하는 함수를 지정할 수 있으므로 융통성도 뛰어나다.
### 한편 key는 min(), max() 내장 함수와도 사용할 수 있다.
### 정렬된 시퀀스의 순서를 유지하면서 항목을 추가하려면 bisect.insort() 메서드를 사용하고, 정렬된 시퀀스를 효율적으로 검색하려면 bisect.bisect() 메서드를 사용하라

## collection.deque 기능이 풍부하고, 스레드 안전한
