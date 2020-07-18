### v-if

- v-if 로 조건문을 걸 수 있습니다.

```html
<div v-if="loading">
</div>
<div v-else>
</div>
```

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
      <div v-if="loading"> <!-- loading 이 true 이면 출력 -->
        Loading...
      </div>
      <div v-else> <!-- loading 이 false 이면 출력 -->
        test user has been logged in
      </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
      new Vue({
        el: '#app',
        data: {
          loading: true
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