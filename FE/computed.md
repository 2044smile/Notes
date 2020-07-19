### computed

- 다른 데이터의 값을 변경시킬 때는 computed 라는 속성을 사용한다.
- 한글 문서에서는 계산된 속성이라고 정의가 나와있다.

#### Example
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <div id="app">
      <p>{{ num }}</p>
      <p>{{ doubleNum }}</p>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
      new Vue({
        el: '#app',
        data: {
          num: 10
        },
        computed: {
          doubleNum: function() {
            return this.num * 2;
          }
        }
      })
    </script>
  </body>
</html>
```

### computed 속성을 이용한 클래스 코드 작성 방법

- computed 속성을 이용한 클래스 코드 작성을 보기 전에 class binding 이라는 것을 이용하여 적용하는 것을 한번 보겠습니다.
#### Class Binding Example
```html
<style>
  .warning {
    color: red;
  }
</style>
<div id="app">
  <p v-bind:class="{ warning: isError}">Hello</p>
  <!-- class binding 
    isError 가 True 면 warning 이 적용되고(빨간색)
  false 이면 warning 이 적용되지 않습니다. -->
</div>
<script>
  new Vue({
    el: '#app',
    data: {
      isError: false
    }
  })
</script>
```

#### Compute Class Binding Example
```html
<style>
  .warning {
    color: red;
  }
</style>
<div id="app">
  <p v-bind:class="errorTextColor">Hello</p>
  <!-- class binding 
    isError 가 True 면 warning 이 적용되고(빨간색)
  false 이면 warning 이 적용되지 않습니다. -->
</div>
<script>
  new Vue({
    el: '#app',
    data: {
      isError: false
    },
    computed: {
      errorTextColor: function(){
        return this.isError ? 'warning' : null; // 3항 연산
      }
    }
  })
</script>
```
