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