# Vuex 란 무엇인가

- Vuex 는 Vue.js 애플리케이션에 대한 **상태 관리 패턴 + 라이브러리** 입니다
- 애플리케이션의 모든 컴포넌트에 대한 **중앙 집중식 저장소 역할**을 하며 예측 가능한 방식으로 상태를 변경할 수 있습니다.
- Vue.js 에서는 상위 컴포넌트, 하위 컴포넌트간 데이터 전달 시 Props 와 Event 를 사용하여 데이터를 송수신 하고, 이벤트를 발생하였는데 이 점을 상태 관리 패턴이라는 이름으로 만든 것이 Vuex 입니다.

## 상태 관리 패턴이란 무엇인가

```javascript
new Vue({
    // 상태(state)
    data () {
        return {
            count: 0
        }
    },
    // 뷰(View)
    template: `
        <div>{{ count }}</div>
    `,
    // 액션(action)
    methods: {
        increment () {
            this.count++
        }
    }
})
```

- 상태(state) 는 앱을 작동하는 원본 소스입니다.
- 뷰는 상태의 선언적 매핑입니다.
- 액션은 뷰에서 사용자 입력에 대해 반응적으로 상태를 바꾸는 방법입니다.

그러나 공통의 상태를 공유하는 여러 컴포넌트가 있는 경우 단순함이 빠르게 저하됩니다.(상위컴포넌트의 data 를 여러 하위컴포넌트가 바라볼 경우)

1. 여러 뷰는 같은 상태에 의존합니다.
2. 서로 다른 뷰의 작업은 동일한 상태를 반영해야 할 수 있습니다.

- 첫 번째 문제의 경우, 지나치게 중첩된 컴포넌트를 통과하는 prop 는 장황할 수 있으며 형제 컴포넌트에서는 작동하지 않습니다.
- 두 번째 문제의 경우 직접 부모/자식 인스턴스를 참조하거나 이벤트를 통해 상태의 여러 복사본을 변경 및 동기화 하려는 등의 해결 방법을 사용해야 합니다. 이러한 패턴은 모두 부서지기 쉽고 유지보수가 불가능한 코드로 빠르게 변경됩니다.

## 상태 관리 패턴 장점

- 상태 관리 및 특정 규칙 적용과 관련된 개념을 정의하고 분리함으로써 코드의 구조와 유지 관리 기능을 향상시킵니다.

## Store

- 모든 Vuex 애플리케이션의 중심에는 Store 가 있습니다. "저장소"는 기본적으로 애플리케이션 상태를 보유하고 있는 컨테이너입니다.
- Vuex Store 는 반응형 입니다. Vue 컴포넌트는 상태를 검색할 때 저장소의 상태가 변경되면 효율적으로 대응하고 업데이트합니다.
- 저장소의 상태를 직접 변경할 수 없습니다. **저장소의 상태를 변경하는 유일한 방법은 명시적인 커밋을 이용한 변이입니다.** 이렇게하면 모든 상태에 대한 추적이 가능하도록 기록이 남을 수 있습니다.
- **저장소의 상태를 직접변경 할 수 있으나 직접 변경하게되면 이력관리를 하지 못하고, 데이터의 변경사항을 디버깅하는데 어려움이 있어 직접변경을 하지말라고 가이드하는 것 같습니다.**

## State

### 단일 상태 트리

- Vuex 는 단일 상태 트리를 사용합니다. 즉, 이 단일 객체는 모든 애플리케이션 수준의 상태를 포함하며 "원본 소스" 역할을 합니다. 이는 각 애플리케이션마다 하나의 저장소만 갖게 된다는 것을 의미합니다.
- 단일 상태 트리를 사용하면 특정 상태를 쉽게 찾을 수 있으므로 디버깅을 위해 현재 앱 상태의 스냅 샷을 쉽게 가져올 수 있습니다.

### Vuex State 를 Vue 컴포넌트에서 가져오기

- Vue 에서 Vuex 저장소에서 상태를 "검색" 하는 가장 간단한 방법은 Compted 속성 내에서 일부 저장소 상태를 가져오는 것 입니다.

```javascript
const Counter = {
    template: `<div>{{ count }}</div>`,
    computed: {
        count() {
            return store.state.count // store 의 상태를 가져와 리턴하면 해당 컴포넌트에서 this 로 사용할 수 있습니다.
        }
    }
}
```

- store.state.count 가 변경되면 Computed 속성이 다시 변경되고 관련 DOM 업데이트가 트리거됩니다.

- 그러나 이 패턴은 컴포넌트가 전역 저장소 단독 항목에 의존하게 됩니다. 모듈 시스템을 사용할 때는 저장소 상태를 사용하는 모든 컴포넌트에서 저장소를 가져와야하며 컴포넌트를 테스트할 때는 가짜데이터가 필요합니다.
- **간단한 한 개의 Vue 파일에서는 위 처럼 사용할 수 있으나 컴포넌트가 여러 개인 경우에는 아래 방법처럼 가져와야된다는 말 같습니다.**

- Vuex 는 `store` 옵션 (Vue.use(Vuex) 에 의해 가능) 으로 루트 컴포넌트의 모든 자식 컴포넌트에 저장소를 "주입" 하는 메커니즘을 제공합니다.

```javascript
const app = new Vue({
    el: '#app',
    // "store" 옵션을 사용하여 저장소를 제공하세요.
    // 그러면 모든 하위 컴포넌트에 저장소 인스턴스가 삽입됩니다.
    store,
    components: { Counter },
    template: `
    <div class="app">
      <counter></counter>
    </div>
})
```

루트 인스턴스에 store 옵션을 제공함으로써 저장소는 루트의 모든 하위 컴포넌트에 주입되고 this.$store 로 사용할 수 있습니다.

```javascript
const Counter = {
    template: `<div>{{ count }}</div>
    computed: {
        count () {
            return this.$store.state.¡count
        }
    }
}
```

## 정리

```javascript
// store.js

import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: { // Vue 인스턴스의 data 와 같다고 보시면 됩니다.
        allUsers: [
            {userId: 'plz1', password: '123', name: 'nick1'}
            {userId: 'plz2', password: '123', name: 'nick2'}
            {userId: 'plz3', password: '123', name: 'nick3'}
        ]
    },
    mutations: {

    },
    actions: {

    }
})
```

## Reference

- [공식문서]('https://vuex.vuejs.org/kr/')
- [공식문서 - state]('https://vuex.vuejs.org/kr/guide/state.html')
- [맨땅에 개발하기]('https://www.youtube.com/watch?v=jdMWiIL-1fk&list=PLZzSdj89sCN292abcbI3utND8pA1T1OyB&index=3')
