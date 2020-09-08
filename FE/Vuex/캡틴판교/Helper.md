# Helper - 각 속성들을 쉽게 사용하는 방법

- state -> mapState
- getters -> mapGetters
- mutations -> mapMutations
- actions -> mapActions

## Helper 사용법

```javascript
import { mapState, mapGetter, mapMutations, mapActions } from 'vuex'

export default {
    computed() {
        ...mapState(['num']), ...mapGetters(['countedNum'])
    },
    methods: {
        ...mapMutations(['clickBtn']), ...mapActions(['asyncClickBtn'])
    }
}
```

### mapState

- Vuex 에 선언한 state 속성을 뷰 컴포넌트에 더 쉽게 연결해주는 헬퍼

```javascript
// App.vue
import { mapState } from 'vuex'

computed() {
    ...mapState(['num'])
    // num() { return this.$store.state.num; }
}

// store.js
state: {
    num: 10
}
```

```html
<!-- <p>{{ this.$store.state.num }}</p>-->
<p>{{ this.num }}</p>
```

### mapGetters

- Vuex 에 선언한 getters 속성을 뷰 컴포넌트에 더 쉽게 연결해주는 헬퍼

```javascript
// App.vue
import { mapGetters } from 'vuex'

computed() { ...mapGetters(['reverseMessage'])}

// store.js
getters: {
    reverseMessage(state) {
        return state.msg.split('').reverse().join('');
    }
}
```

```html
<!-- <p>{{ this.$store.getters.reverseMessage </p>-->
<p>{{ this.reverseMessage }}</p>
```

### mapMutations

```javascript
// App.vue
import { mapMutations } from 'vuex'

methods: {
    ...mapMutations(['clickBtn']),
    authLogin() {},
    displaoyTable() {}
}

// store.js
mutations: {
    clickBtn(state) {
        alert(state.msg);
    }
}
```

```html
<button @click="clickBtn">popup</button>
```

1. Client 가 버튼을 클릭하면 methods 의 ...mapMutations 가 동작하게되고, mutations으로 이동하여 clickBtn 이 실행되고, alert 알람이 뜨게 됩니다.

### mapActions

```javascript
// App.vue
import { mapAction } from 'vuex'

methods: {
    ...mapActions(['delayClickBtn'])
}

// store.js
actions: {
    delayClickBtn(context) {
        setTimeout(() => context.commit('clickBtn'), 2000)
    }
}
```

```html
<button @click="delayClickBtn">delay popup message</button>></button>
```

## Helper의 유연한 문법

- Vuex 에 선언한 속성을 그대로 컴포넌트에 연결하는 문법

```javascript
// 배열 리터럴
...mapMutations([
    'clickBtn', //'clickBtn': clickBtn
    'addNumber' // 이렇게 명시해두면 clickBtn에 알아서 인자를 전달해줍니다.
])
```
- Vuex 선언한 속성을 컴포넌트의 특정 메서드에다가 연결하는 문법

```javascript
// 객체 리터럴
...mapMutations({
    popupMsg: 'clickBtn' // 컴포넌트 메서드 명: Store의 Mutations 명
})
```

### 인자

- 이벤트를 클릭하는 부분에서 인자를 넘겨주고 map 헬퍼를 사용하면 인자를 명시하여 넘겨줄 필요가 없습니다.
