### derective & v-bind
- 특정 데이터의 값이 HTML 의 ID, CLASS 같은 곳에 연결이 된다고 생각하면 됩니다.
- 전체적인 DOM 을 변경할 수 있다.
- v-bind 를 명시하면 Vue에서 데이터를 가져온다고 생각하면 된다.


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
      <p v-bind:id="uuid" v-bind:class="name">{{ num }}</p>
      <p>{{ doubleNum }}</p>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
      new Vue({
        el: '#app',
        data: {
          num: 10,
          uuid: 'abcd1234',
          name: 'text-blue'
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