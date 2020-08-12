# ModelViewSet lookup_fields

## 문제
- ModelViewSet에 drf-yasg 를 연결하여 사용하는데 retrieve, patch, put . . 같은 경우에 lookup_fields 가 Default 로 id(pk) 로 되어있는 것을 user_id 로 변경하라

## 해결
- lookup_fields 라는 것을 ModelViewSet 안에 변수로 지정하고, 원하는 값으로 변경해주면 됩니다.

```python
class FooBarViewSet(viewsets.ModelViewSet):

    permission_classes = (RequiresUserId,)
    queryset = FooBar.objects.all()
    ordering = ['-created_at']
    lookup_field = 'user_id'
```
- example) foobar/update/<user_id>/ 이런식으로 변경됩니다.