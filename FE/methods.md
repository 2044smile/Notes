### methods

- methods 로 함수를 생성해두고 컨트롤 할 수 있습니다.
- v-on:keyup.enter="logText" enter 기가 눌리면 logText 라는 메소드가 실행이 됩니다.
- 전에 배웠지만 v-on:click 으로도 메소드를 실행시킬 수 있습니다.
- 위 설명을 보면 알 수 있듯이 어디선가 methods 를 트리거해야만 실행된다는 것을 알 수 있습니다.


#### Example
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
        <button v-on:click="logText">click me</button>
        <input type="text" v-on:keyup.enter="logText">
        <button>Add</button>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        new Vue({
            el: '#app',
            methods: {
                logText: function() {
                    console.log('clicked');
                                        
                }
            }
        })
    </script>
</body>
</html>
```