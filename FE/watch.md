### watch
- 기본적으로 데이터를 대상으로 열 수 있고, 데이터의 변환에 따라서 특정 로직을 실행할 수 있는 뷰의 속성입니다.
- watch 는 감시자의 역할을 한다고 이해하면 됩니다.
- 지정한 대상의 값이 변경될 때 마다 정의한 함수가 실행됩니다.
```javascript
new Vue({
    el: '#app',
    data: {
        count: 3,
        text: 'Before the change'
    },
    watch: {
        count: function(newVal, oldVal) {
            this.text = oldVal + '에서 ' + newVal + '로 변경되었습니다'
        }
    }
})
```
- 위 코드에서 watch 는 count 라는 값을 감시하고 있습니다. count 의 값이 변화 할 때 마다 watch 안에 정의한 count 라는 함수가 실행되는 것 입니다.
- newVal, oldVal 과 같이 변경 전의 값을 인자로 받을 수 있습니다.
- computed 와 비슷해보이는데 차이점은 무엇을까?

### watch vs computed
- **computed** 벨리데이션하는데 주로 사용
- **watch** 무거운 데이터 작업
- compute 가 계산된 값을 출력하는 용도라면, watch 는 어떤 조건이 되었을 때 함수를 실행시키기 위한 트리거로서 사용할 수 있습니다.
- Vue 공식문서에서는 watch 대신에 computed 를 사용하는 것을 추천한다.

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
      {{ num }}
      <button v-on:click="addNum">increase</button>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
      new Vue({
        el: "#app",
        data: {
          num: 10,
        },
        watch: {
          num: function() {  // num 은 data의 num을 가리킨다.
            this.logText;
          }
        },
        methods: {
          addNum: function () {
            this.num = this.num + 1;
          },
          logText: function() {
            console.log('changed');
          }
        },
      });
    </script>
  </body>
</html>
```