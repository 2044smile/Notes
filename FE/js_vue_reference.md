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

## 실습 (투두리스트 만들기)

```commandline
>>> vue create todo

Please pick a preset: default (babel, eslint)
>>> enter
```
### 디렉터리 구조 설명

- node_modules: 개발에 필요한 패키지들이 설치되어있다.
- public: favicon.ico, index.html <div id="app"> vue js를 라우트 할 div 태그가 있습니다.
- src: 
  - webpack 이 파일을 읽어들일 시작 지점인 main.js 파일 
  - 기본 예제인 components/HelloWorld.vue
- root:
  - babel.config.js: 바벨 설정
  - package.json: same to requirements
    - serve, build, lint
      - serve: 로컬 웹 서버를 돌려 내가 개발한 코드를 실시간으로 확인할 수 있는 스크립트
      - build: 개발 완료 후 서버에 올릴 파일들을 생성하는 스크립트 입니다.
      - lint: 스크립트 문법을 체크하는 용도, vuejs 관련 내용은 아니다.


## 명령

- run server
```commandline
npm run serve
```
- script ( vue code )
```script
export defualt { 
    name: 'App' // App.vue
    data() {  // v-model 에서 데이터를 가져오거나 할 때 사용하기에 적합하다.
        return {
            userInput: '',
            todoList: []
        };
    },
    conputed: {  // 값을 변경할 때 주로 사용한다. getter 함수처럼 동작한다.
        activeTodoList() {
            return this.todoList.filter(todo => todo.state === 'active')
        }
    },
    methods: {
    // 메소드라는 것은 단순히 값을 가져오기 보다는 메소드 호출 시 내부 값을 변경하거나
    // axios 로 외부 값을 읽어 들이거나 내부 상태 값을 변경시키는데 사용된다.
        addNewTodo() {
            this.todoList.push({
                label: this.userInput,
                state: 'active'
            });
            this.userInput = '';
        },
        toggleTodoState(todo) {
            todo.state = todo.state === 'active' ? 'done' : 'active'; // python의 삼항연산과 비슷
        }
    },
}
```

## Component
1. component 폴더 안에 Todo.vue라는 파일을 생성해주겠습니다.
```html
<templete>
    <button class="list-group-item text-left" @click="clickButton"">
        {{ label }}
    </button>
</templete>
<script>
    export default {
        props: ['label'],  // 여기를 props 로 지정하면서 html 코드가 {{ todo.label }} 에서 {{ label }}로 변경됩니다.
        methods: {
            clickButton(){
                this.$emit('componentClick') 
            }       
        }
    };
</script>

<!-- 이렇게 만들어주고 난 뒤 App.vue로 이동해서 import 를 해줍니다. -->
import Todo from './components/Todo';

그리고 Vue 코드 안에
components: {
    Todo,
}

위와 같이 설정해주고,

template 부분에서

<todo
    :label=""todo.label"
    @componentClick="toggleTodoState(todo)"
/>
```

### App.vue
위 파일은 보통 컴포넌트를 import 하거나 생성한 뷰를 HTML 엘리먼트에 마운트 시킵니다.


### SPA 가 아닌 MVC 에서 사용할 때 FLOW
만들어둔 Vue 코드를 SPA 가 아닌 MVC 를 사용하는 프레임워크에서 사용할 때는
vue, vue-loader, vue-template-compiler를 설치하고, 웹팩 설정(webpack.config.js)을 해준 뒤 app.js 파일에서 
Vue를 마운트 시켜줍니다. 마운트란 어떠한 HTML 엘리먼트에서 사용할지와 사용할 컴포넌트를 지정해줍니다.
그리고 뷰를 마운트할 엘리먼트를 생성해주고, 컴포넌트를 사용하면 됩니다.
 

## Reference

- 레시피 Vue 강의
  https://www.youtube.com/watch?v=BWb-_pvmwyU&list=PLwawSyI26pfuGsEzp7AzP_TJVhSdwFuwh&index=6
- https://blog.metafor.kr/202
- 드림코딩
  https://www.youtube.com/watch?v=wcsVjmHrUQg&list=PLv2d7VI9OotTVOL4QmPfvJWPJvkmv6h-2
- https://kr.vuejs.org/v2/guide/index.html
- 캡틴 판교님
  - https://joshua1988.github.io/web-development/javascript/promise-for-beginners/