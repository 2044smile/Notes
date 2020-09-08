# state and getters

## Vuex 기술 요소

- state: 여러 컴포넌트에 공유되는 데이터 `data`
- getters: 연산된 state 값을 접근하는 속성 `computed`
- mutations: state 값을 변경하는 이벤트 로직 & 메서드 `methods`
- actions: 비동기 처리 로직을 선언하는 메서드 `aysnc methods`

 ### State

 - 여러 컴포넌트 간에 공유할 데이터 - 상태

```javascript
// Vue
data: {
    message: 'Hello Vue.js!'
}

// Vuex
state: {
    message: 'Hello Vue.js!'
}
```

```html
<!-- Vue -->
<p>{{ message }}</p>

<!-- Vuex -->
<p>{{ this.$store.state.message }}</p>
```

### Getters

- state 값을 접근하는 속성이자 `computed()` 처럼 미리 연산된 값을 접근하는 속성

```javascript
// store.js
state: {
    num: 10
},
getters: {
    getNumber(state) {
        return state.num;
    },
    doubleNumber(state) {
        return state.num * 2
    }
}
```

```html
<p>{{ this.$store.getters.getNumber }}</p>
<p>{{ this.$store.getters.doubleNumber }}</p>
```

### store.js 구조

- store.js 내에서도 localStorage 관련 코드를 나눠서 관리해주는데 좋은거같다.

```javascript
import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

const storage = {
  fetch() {
    const arr = [];
    if (localStorage.length > 0) {
      for (let i = 0; i < localStorage.length; i++) {
        if (
          localStorage.key(i) !== "loglevel:webpack-dev-server" &&
          localStorage.key(i) !== ""
        ) {
          arr.push(JSON.parse(localStorage.getItem(localStorage.key(i))));
        }
      }
    }
    return arr;
  },
};

export const store = new Vuex.Store({
  state: {
    todoItems: storage.fetch()
  },
});

```