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

### Event Emit
- 상위 컴포넌트에서는 하위 컴포넌트로 props 로 데이터를 전달하고,
- 하위 컴포넌트에서는 상위 컴포넌트로 이벤트를 발생시키게 됩니다.

### Example
```javascript
var appHeader = {
    template: '<button v-on:click="passEvent">Click Me</button>',  // 1
    methods: {
        passEvent: function() {  // 2
            this.$emit('pass')  // 3
        }
      }
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
```
위 상태로 버튼을 클릭하면 Vue Tools 에서 이벤트를 보면 pass 라는 값이 찍히는 것을 확인할 수 있습니다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div id="app">
        <h1>Hello</h1>
        <!-- <app-header v-on:하위 컴포넌트에서 발생한 이벤트 이름="상위 컴포넌트의 메서드 이름"></app-header> -->
        <app-header v-on:pass="logText"></app-header>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        var appHeader = {
            template: '<button v-on:click="passEvent">Click Me</button>',
            methods: {
                passEvent: function() {
                    this.$emit('pass')  // pass 라는 이벤트를 발생
                }
            }
        }
        new Vue({
            el: "#app",
            components: {
                'app-header': appHeader
            },
            methods: {
                logText: function() {
                    console.log("Hi");
                }
            }
        })
    </script>
</body>
</html>

```