### Props

#### 명령어 사용법

```html
<app-header v-bine:프롭스 속성 이름="상위 컴포넌트의 데이터 이름"></app-header>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div id="app">
        <!-- <app-header v-bind:프롭스 속성 이름="상위 컴포넌트의 데이터 이름"></app-header> -->
        <app-header v-bind:propsdata="message"></app-header>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        var appHeader = {
            template: '<h1>header</h1>',
            props: ['propsdata']
        }

        new Vue({
            el: '#app',
            components: {
                'app-header': appHeader
            },
            data: {
                message: 'Hi'
            }
        })
    </script>
</body>
</html>
```

#### 특징
- 리액티비티가 프롭스에도 적용이 된다. 그 예시로는 루트의 데이터 값을 변경하면 하위 컴포넌트의 데이터도 같이 변경된다.
