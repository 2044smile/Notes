# mutations and commit

## mutations

- state 의 값을 변경할 수 있는 유일한 방법이자 메서드
- mutations는 commit() 으로 동작시킨다.

```javascript
// store.js
state: { num : 10 },
mutations: {
    printNumbers(state) {
        return state.num
    },
    sumNumbers(state, anotherNum){
        return state.num + anotherNum;
    }
}

// App.vue
this.$store.commit('printNumbers');
this.$store.commit('sumNumbers', 20);
```

## commit 형식

- state 를 변경하기 위해 mutations 를 동작시킬 때 인자(payload) 를 전달할 수 있음

```javascript
// store.js
state: { storeNum: 10 },
mutations: {
    modifyState(state, payload) {
        console.log(payload.str)
        return state.storeNum + payload.num;
    }
}

// App.vue
this.$store.commit('modifyState', {
    str: 'passed from payload',
    num: 20
})
```

### Why use to mutation

- 여러 개의 컴포넌트에서 아래와 같이 state 값을 변경하는 경우 어느 컴포넌트에서 해당 state 를 변경했는지 추적하기 어렵다.

```javascript
methods: {
    increaseCounter() { this.$store.state.counter++; }
}
```

- 특정 시점에 어떤 컴포넌트가 state를 접근하여 변경한 건지 확인하기 어렵기 때문
- 따라서, 뷰의 반응성을 거스르지 않게 명시적으로 상태 변화를 수행. 반응성, 디버깅, 테스팅 기능 제공

