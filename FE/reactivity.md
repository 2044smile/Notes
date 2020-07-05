### Reactivity 라이브러리화 구현 예시
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Vue-Way</title>
  </head>
  <body>
    <div id="app"></div>
    <script>
      var div = document.querySelector("#app");
      var viewModel = {};
      (function () { // 즉시 실행함수
        function init() {
          Object.defineProperty(viewModel, "str", {
            // 속성에 접근했을 때의 동작을 정의
            get: function () {
              console.log("GET");
            },
            // 속성에 값을 수정했을 때의 동작을 정의
            set: function (newValue) {
              render(newValue);
            },
          });
        }

        function render(value) {
          div.innerHTML = value;
        }

        init();
      })();
    </script>
  </body>
</html>

```

### 즉시 실행함수
위에서 즉시 실행함수를 사용한 이유는 라이브러리 내부 로직이 사용자에게 노출되지 않도록 변수 유효 범위를 분리하기 위해서이다.