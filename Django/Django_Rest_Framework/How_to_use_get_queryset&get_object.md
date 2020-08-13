# How to use get_queryset & get_objects

## get_queryset

- get_queryset 을 알아보기 전에 ViewSet 의 queryset 에 대해 잠깐 알아보면 queryset에 명시 된 쿼리가 돌고 그 쿼리를 viewset의 여러 action 들 list, create, retrieve, update, partial_update, destroy 에서 한번 호출되어 사용할 수 있습니다.

```python
class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
```

- 먼저 어떻게 사용할 수 있는지 예시를 살펴보도록 하겠습니다.

**해당 내용은 Blog 에 자세히 포스팅**