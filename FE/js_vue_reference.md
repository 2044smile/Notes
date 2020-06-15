## 정리

- 사용자 입력값과 자바스크립트 변수값을 동기화 시키는 v-model
```html
<div id="app">
    <input type="text" v-model="message">
    <p>message: {{ message }}</p>
</div>
```
```javascript
new Vue({
    el: '#app',
    data: {
        message: ''    
    }
})
```
- 리스트를 출력하는 v-for
```html
<ul id="app">
    <li v-for="item in items">
        {{ item.message }}
    </li>
</ul>
```
```javascript
var app = new Vue({
    el: '#app',
    data: { 
        items: [
            { message: 'Foo'},
            { message: 'Bar'},
        ]   
    }
})
```
- 태그 Attribute 자바스크립트 변수값을 대입하는 v-bind 혹 : 보통 : 으로 함축하여 사용한다.
```html
<img v-bind:src="" alt="">
<img :src="" alt="">
```
- 메소드 정의, 이벤트를 연결하는 v-on 혹은 @
```html
<div id="app">
    <button type="button" v-on:click="add">더하기</button>
    {{ counter }}

    <input type="text" @keyup.enter="keyUp">
</div>
```
```javascript
let app = new Vue({  // 인스턴스 생성
    el: '#app',
    data() {
        return {  // data 메서드
            counter: 0
        };
    },
    methods: {
        add() {
            this.counter ++;
            console.log(this.counter)
        },
        keyUp(ev) {
            if (ev.keyCode !== 13) {
                console.log('엔터키 아님');
                return;
            }

            console.log('엔터키 눌림');
        }
    }
})
```

## SPA(Single Page Application)


## Reference

- https://www.youtube.com/watch?v=BWb-_pvmwyU&list=PLwawSyI26pfuGsEzp7AzP_TJVhSdwFuwh&index=6
- https://blog.metafor.kr/202
- https://www.youtube.com/watch?v=wcsVjmHrUQg&list=PLv2d7VI9OotTVOL4QmPfvJWPJvkmv6h-2
- https://kr.vuejs.org/v2/guide/index.html