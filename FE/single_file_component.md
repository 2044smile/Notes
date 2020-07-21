### single file component
- 싱글 파일 컴포넌트란 무엇일까?
  - 아주 간단하게는 .vue 확장자를 가진 것을 싱글 파일 컴포넌트라고 생각하면 됩니다.
- 싱글 팡리 컴포넌트는 우리가 여태까지 배웠던 뷰를 사용하는 방식과는 많이 다릅니다. 아래 공식문서에서 가져온 예제를 살펴보겠습니다.
- 싱글 파일 컴포넌트를 사용하면서 생기는 이점
1. 완전한 구문 강조
2. CommonJS 모듈
3. 컴포넌트에만 제한된 CSS

#### Example
```javascript
<template>
    <p>{{ greeting }} World!</p>
</template>

<script>
module.exports = {
    data: function() {
        return {
            greeting: 'Hello'
        }
    }
}
</script>

<style>
p {
    font-size: 2em;
    text-align: center;
}
</style>
```

### Reference
- https://kr.vuejs.org/v2/guide/single-file-components.html