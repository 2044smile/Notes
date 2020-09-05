# 클래스와 스타일 바인딩

## HTML 클래스 바인딩하기

**객체 구문**

- 클래스를 동적으로 토글하기 위해 v-bind:class 에 객체를 전달할 수 있습니다.

```html
<div v-bind:class="{ active: isActive}"></div>
```

위 구문은 active 클래스의 존재 여부가 데이터 속성 isActive의 참 속성에 의해 결정되는 것을 의미합니다. 객체에 필드가 더 있으면 여러 클래스를 토글 할 수 있습니다. 또한 v-bind:class 디렉티브는 일반 class 속성과 공존할 수 있습니다. 그래서 다음과 같은 템플릿이 가능합니다.

- 정리해보자면 isActive 라는 값이 True 라면 active 가 클래스에 바인딩 된다는 것 입니다.

## 인라인 스타일 바인딩

**객체 구문**

- v-bind:style 객체 구문은 매우 직설적입니다. 거의 CSS 처럼 보이지만 JavaScript 객체입니다. 속성 이름에 camelCase 와 kebab-cade를 사용할 수 있습니다.

```html
<div v-bind:style="{color: activeColor, fontSize: fontSize + 'px' }"></div>

<script>
data: {
    activeColor: 'red',
    fontSize: 30
}
</script>
```

위 처럼 인라인 스타일로 작성할 수도 있지만 스타일 객체에 직접 바인딩 하여 템플릿이 더 간결하도록 만드는 것이 좋습니다.

```html
<div v-bind:style="styleObject"></div>

<script>
data: {
    styleObject: {
        color: 'red',
        fontSize: '13px'
    }
}
</script>
```
