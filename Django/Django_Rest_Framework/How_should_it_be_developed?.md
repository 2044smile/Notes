# How should it be developed?

## Django REST Framework
1. [비지니스 로직을 넣을 위치]('http://engineering.vcnc.co.kr/2018/05/parquet-and-spark/')
- 애플리케이션의 비지니스 로직을 어디에 어떻게 두어야하는지 설명하는 방식으로 간단한 사용자와 팔로워 예시를 들어 실제 예제로 보여드리겠습니다.
사용자(Django 기본값), 게시물, 팔로워 (다 대다) 테이블이 있습니다. 요컨대, 비지니스 로직을 배치하는 가장 좋은 위치는 serializer 입니다.

- 공식문서에 따르면 Serializer 를 사용하면 쿼리 세트 및 모델 인스턴스와 같은 복잡한 데이터를 JSON, XML 또는 다른 콘텐츠 유형으로 쉽게 렌더링 할 수 있는
네이티브 Python 데이터 유형으로 변환할 수 있습니다.

- Serializer 는 또한 Deserialization 을 제공하여 들어오는 데이터의 유효성을 검사 한 후 구문 분석 된 데이터를 복잡한 형식으로 다시 변환할 수 있습니다.

## CASE
```python
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()  # get Django default User 


class Followers(models.Model):
    follower = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_followers'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_following'
    )
    show_feed = models.BooleanField(default=False)


class Post(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeFied(auto_now_add=True)
```

- 다른 사용자를 팔로우한 사용자의 경우 다음 URL에 POST 요청을 수행하여 추적하려는 사용자 ID를 제공해야합니다.
```/api/users/<user_id_to_follow>/follow/```

- 팔로우하려는 사용자 ID 와 현재 사용자를 입력한 뷰에서 get_serializer_context 메서드를 재정의하여 이를 수행합니다.
```python
from rest_framework import generics

from .serializers import FollowUserSerializer


class FollowUserAPIView(generics.CreateAPIView):
    serializer_class = FollowUserSerializer

    def get_serializer_context(self):
        context = (
            super(FollowUserAPIView, self)    # FollowUserSerializer 의 self.context의 정보를 가져와 context에 담고
            .get_serializer_context()
        )
        context.update({  # context 를 업데이트해줍니다, 실제 사용예시를 들면 self.context['follow_id'] 가 되겠죠?
            'follow_id': self.kwargs.get('id'),
            'current_user': self.request.user
        })
        return context
```

- 마지막으로 Serializer 클래스는 데이터베이스 객체 생성을 수행합니다.
```python
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.db import transaction
from rest_framework import serializers

from posts.models import Post
from .models import Followers

User = get_user_model()


class FollowUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Followers
        fields =['show_feed']

    @transaction.atomic
    def create(self, validated_data):
        follow_id = self.context.get('follow_id')
        follower = self.context.get('current_user')
        follow_obj = get_object_or_404(User, id=follow_id)

        Post.objects.create(
            context="{0} started following {1}".format(
                follower.username,
                follow_obj.username
            )
        )

        return Followers.objects.create(
            follower = follower,
            following = follow-obj,
            **validated_data
        )
```
- create 메서드를 재정의하여 팔로우하려는 사용자 ID와 현재 사용자를 추출합니다. 팔로우하고자하는 사용자가 존재하는지 확인한 후,
한 사용자가 다른 사용자를 팔로우하기 시작한 콘텐츠가 포함 된 간단한 게시물을 데이터베이스에 추가합니다. 마지막으로 구체적인 팔로워 모델을 데이터베이스에
추가했습니다. **Create 메서드는 원자적(atomic)이므로 트랜잭션 중 하나라도 실패하면 모두 되돌립니다.**

## 결론
- **모든 비지니스 로직은 Serializer 에 넣으십시오. 많은 Serializer 메서드에서 사용되는 일반적인 항목은 utils.py 또는 관련 폴더를 만들어서 관리하는 것도 좋아보입니다.**