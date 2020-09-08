# Actions

- 비동기 처리 로직을 선언하는 메서드 (비동기 로직을 담당하는 mutations)
- 데이터 요청, Promise, ES6 async과 같은 비동기 처리는 모두 actions에 선언

```javascript
// store.js
state: {
    num: 10
},
mutations: {
    doubleNumber(state) {
        state.num * 2
    }
},
actions: {
    delayDoubleNumber(context) { // context로 store의 메서드 속성 접근
        context.commit('doubleNumber');
    }
}

// App.vue
this.$store.dispatch('delayDoubleNumber')
```

## 왜 비동기 로직은 actions 에 선언해야 할까

- 언제 어느 컴포넌트에서 해당 state를 호출하고, 변경했는지 확인하기 어려움
- state 값의 변화를 추적하기 어렵기 때문에 mutations 속성에는 동기 처리 로직만 넣어야 한다.

## 정리

```javascript
// store.js
mutations: {
    setData(state, fetchedData) {
        state.product = fetchedData;
    }
},
actions: {
    fetchProductData(context) {
        return axios.get('https://domain.com/products/1').then(response => context.commit('setData', response));
    }
}

// App.vue
methods: {
    getProduct() {
        this.$store.dispatch('fetchProductData');
    }
}
```

- 위 예제 참고 flow

1. 컴포넌트 methods 에서 actions 를 dispatch
2. actions 에서 직접 state 의 값을 변경하지 않고, context 라는 인자에 .commit 메서드를 사용하여 mutations 에 변화를 줍니다.
3. mutations 는 commit 이 감지되면 state.product 의 값에 fetchedData를 넣게됩니다.
