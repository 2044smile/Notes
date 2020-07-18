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