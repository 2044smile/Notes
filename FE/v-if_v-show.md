### v-if & v-show

- 조건부 렌더링을 할 때 사용하는 디렉티브는 v-if 와 v-show 가 있습니다.
- v-if 로 조건문을 걸 수 있습니다.

#### v-if
- ok의 값이 참이면 Yes 가 렌더링되고, 거짓이면 No가 렌더링 됩니다.
- v-else 를 통해서 else 블록을 나타낼 수도 있습니다.

```html
<h1 v-if="ok">yes</h1>
<h1 v-else>yes</h1>

<template v-if="ok">
    <h1>Hello</h1>
</template>
```

#### v-show
- v-if 와 거의 동작이 비슷하다.
- ok 값이 참이면 화면에 표시된다.

```html
<h1 v-show="ok">Yes</h1>
```


#### 차이점
- v-if 는 조건에 따라 컴포넌트가 실제로 제거되고 생성된다.
- 반면에 v-show는 단순히 CSS 의 display 속성만 변경된다.
  - display: none, display: block 의 차이다. 초기 렌더링 때 DOM에 유지 된다.
- 사소한 차이지만 우리는 경우에 따라 v-if, v-show 디렉티브를 나눠서 사용할 수 있습니다.
  - toggle 작업이 자주 일어나는 경우 v-show가 유리하고 그 반대의 경우에는 v-if 가 유리합니다.


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
      <input type="text" v-model="msg">
      <p>{{ msg }}</p>
      <div v-if="loading"> <!-- loading 이 true 이면 출력 -->
        Loading...
      </div>
      <div v-else> <!-- loading 이 false 이면 출력 -->
        test user has been logged in
      </div>
      <div v-show="loading">
        Loading...
      </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
      new Vue({
        el: '#app',
        data: {
          loading: true,
          msg: ''
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