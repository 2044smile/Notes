## API 최적화

- 쿼리에 대한 문제로 인한 성능저하 발생 ( N + 1 쿼리 )

- prefetch_related() 를 적용하였는데도 문제를 발생
  - 2-level 까지 많은 다른 테이블들을 전부 조인
  
문제
1. 계산하는 Field 를 가진 Serializer 의 경우
- annotate 로 먼저 계산을 해놓는 방법으로 해결

2. 조건적인 queryset을 prefetch 해야하는 경우
- 복잡한 조건을 가지고 있더라도 Subquery(), Case(), when() 를 사용하여 성능향상
```
prefetched_iamges = A.objects.filter(is_active=True)
Prefetch('images', prefetchd_images)
```

3. 코드가 지저분해진다.
- Serializer 안에 
```
class Serializer()
    user = CustomerSerializer()
```

prefetch 를 하더라도 어노테이트를 하니 오래걸린다.
그래서 시리얼라이저에서 계산을 해주고 처리를하여 시간이 

django-cachalot
@cache_page()
 