## 공식문서 정리

### JavaScript 표현식 사용

```javascript
{{ number + 1 }}

{{ ok ? 'YES' : 'NO ' }}  // if 연산은 지원하지 않습니다, 삼항 연산자를 사용해야 합니다.

{{ message.split('').reverse().join('') }}
```

### 디렉티브
- 디렉티브는 v- 접두사가 있는 특수 속성입니다.
- 디렉티브 속성 값은 단일 JavaScript 표현식이 됩니다.( 나중에 설명 할 v-for 는 예외입니다. )
- 디렉티브의 역할은 표현식의 값이 변경될 때 사이드이페트를 반응적으로 DOM 에 적용하는 것 입니다.

```html
<p v-if="seen">이제 나를 볼 수 있어요</p>
```
- 위 예시에 v-if 디렉티브는 seen 이 False 라면 p 엘리먼트를 제거하고, True 라면 삽입합니다.

### 전달인자
- 일부 디렉티브는 콜론으로 표시되는 "전달인자" 를 사용할 수 있습니다.
- 예를 들어, v-bind(:) 디렉티브는 반응적으로 HTML 속성을 갱신하는데 사용됩니다.

```html
<a v-bind:href="url">. . .</a>
```
- 여기서 href 는 전달인자로, 엘리먼트의 href 속성을 표현식 url 의 값에 바인드하는 v-bind 디렉티브에게 알려줍니다.
- JavaScript 변수 값도 대입할 수 있습니다.

```html
<a v-on:click="doSomething">. . .</a>
```
전달인자는 이벤트를 받을 이름입니다.

### computed
- 템플릿 내에 표현식을 넣으면 편리합니다. 하지만 간단한 연산일 때만 이용하는 것이 좋습니다.
- 복잡한 로직이라면 반드시 computed 속성을 사용해야 하빈다.

```html
<div id="example">
    <p>원본 세미지: "{{ message }}" </p>
    <p>역순 메시지: "{{ reversedMessage }}" </p>
</div>
```
```javascript
var vm = new Vue({
    el: '#example',
    data: {
        message: 'Hello'  // this.message 가 가리키는 곳
    },
    computed: {
        // 계산 된 getter
        reversedMessage: function() {
            // 'this' 는 vm 인스턴스를 가리킵니다.
            return this.message.split('').reverse().join('')
        }
    }
})
```

### computed 속성의 캐싱 vs 메소드
- 표현식에서 메소드를 호출하여 같은 결과를 얻을 수도 있습니다.
```html
<p>뒤집힌 메시지: "{{ reversedMessage() }}"</p>
```

- 정리해보면 computed 속성 대신 메소드와 같은 함수를 정의할 수도 있습니다.
- 최종 결과에 대해 두 가지 접근 방식은 서로 동일합니다.
- **차이점은 computed 속성은 종속 대상을 따라 저장(캐싱) 된다는 것 입니다.**
- **computed 속성은 해당 속성이 종속된 대상이 변경될 때만 함수를 실행합니다. 즉 message 가 변경되지 않는 한, computed 속성인
reversedMessage 를 여러 번 요청해도 계산을 다시하지 않고 계산되어 있던 결과를 즉시 반환합니다.**

- 또한 Date.now() 처럼 아무 곳에도 의존하지 않는 computed 속성의 경우 절대로 업데이트되지 않는다는 뜻 입니다.
```javascript
computed: {
    now: function () {
        return Date.now()
    }
}
```
이에 비해 메소드를 호출하면 렌더링을 다시 할 때마다 항상 함수를 실행합니다.

- 그렇다면 캐싱이 왜 필요할까요? 계산에 시간이 많이 걸리는 computed 속성인 A 를 가지고 있다고 해봅시다.
이 속성을 계산하려면 거대한 배열을 반복해서 다루고 많은 계산을 해야 합니다. 그런데 A 에 의존하는 다른 computed 속성값도 있을 수 있습니다.
캐싱하지 않으면 A 의 getter 함수를 꼭 필요한 것 보다 더 많이 실행하게 됩니다! 캐싱을 원하지 않는 경우 메소드를 사용하십시오.

### computed vs watch
- Vue 는 Vue 인스턴스의 데이터 변경을 관찰하고 이에 반응하는 보다 일반적인 watch 속성을 제공합니다.
다른 데이터 기반으로 변경할 필요가 있는 데이터가 있는 경우 watch 를 남용하는 경우가 있는데 하지만 명령적인
watch 콜백보다 computed 속성을 사용하는 것이 더 좋습니다.
- watch 속성은 감시할 데이터를 지정하고 그 데이터가 바뀌면 이런 함수를 실행하라는 방식으로 소프트웨어 공학에서 이야기하는 '명령형 프로그래밍' 방식
- computed 속성은 계산해야 하는 목표 데이터를 정의하는 방식으로 소프트웨어 공학에서 이야기하는 '선언형 프로그래밍' 방식

```html
<div id="demo">
    {{ fullName}}
</div>
```
```javascript
var vm = new Vue({
      el: '#demo',
      data: {
        firstName: 'Foo',
        lastName: 'Bar',
        fullName: 'Foo Bar'
      },
      watch: {
        firstName: function (val) {
          this.fullName = val + ' ' + this.lastName
        },
        lastName: function (val) {
          this.fullName = this.firstName + ' ' + val
        }
      }
})

-- console --
vm.firstName = 'lee' // 로 변경할 때 watch 가 작동됩니다.
vm.lastName = 'changseok' // 로 변경할 때 watch 가 작동됩니다.
```

같은 코드를 computed 로 작성하면

```javascript
var vm = new Vue({
    el: '#demo',
    data: {
        firstName: 'Foo',
        lastName: 'Bar'
    },
    computed: {
        fullName: function () {
            return this.fullName + ' ' + this.lastName
        }
    }
})
```

- 일반적으로 선언형 프로그래밍이 명령형 프로그래밍보다 코드 반복이 적은 등 우수하다고 평가하는 경향이 있습니다.

### computed 속성의 setter 함수
- 기본적으로 getter 함수만 가지고 있지만, 필요한 경우 setter 함수를 만들어 사용할 수 있습니다.

```javascript
computed: {
  fullName: {
    // getter
    get: function () {  // fullName 호출 시 인스턴스에서 선언한 값이 리턴 됨
      return this.firstName + ' ' + this.lastName
    },
    // setter
    set: function (newValue) {  // input: changseok lee 
      var names = newValue.split(' ')
      this.firstName = names[0]  // changseok
      this.lastName = names[names.length - 1]  // lee
    }
  }
}
```

### watch 속성
- 대부분의 경우 computed 속성이 더 적합하지만 사용자가 만든 감시자가 필요한 경우가 있습니다.
그래서 Vue 는 watch 옵션을 통해 데이터 변경에 반응하는 보다 일반적인 방법을 제공합니다. 이는 **데이터 변경에 대한 응답으로 비동기식
또는 시간이 많이 소요되는 조작을 수행하려는 경우에 가장 유용합니다.**

```html
<div id="watch-example">
    <p>
        yes/no 질문을 물어보세요:
        <input v-model="question">    
    </p>
    <p>{{ answer }}</p>
</div>
```

```javascript
<!-- 이미 Ajax 라이브러리의 풍부한 생태계와 범용 유틸리티 메소드 컬렉션이 있기 때문에, -->
<!-- Vue 코어는 다시 만들지 않아 작게 유지됩니다. -->
<!-- 이것은 이미 익숙한 것을 선택할 수 있는 자유를 줍니다. -->
<script src="https://unpkg.com/axios@0.12.0/dist/axios.min.js"></script>
<script src="https://unpkg.com/lodash@4.13.1/lodash.min.js"></script>
<script>
var watchExampleVM = new Vue({
  el: '#watch-example',
  data: {
    question: '',
    answer: '질문을 하기 전까지는 대답할 수 없습니다.'
  },
  watch: {
    // 질문이 변경될 때 마다 이 기능이 실행됩니다.
    question: function (newQuestion) {
      this.answer = '입력을 기다리는 중...'
      this.getAnswer()
    }
  },
  methods: {
    // _.debounce는 lodash가 제공하는 기능으로
    // 특히 시간이 많이 소요되는 작업을 실행할 수 있는 빈도를 제한합니다.
    // 이 경우, 우리는 yesno.wtf/api 에 액세스 하는 빈도를 제한하고,
    // 사용자가 ajax요청을 하기 전에 타이핑을 완전히 마칠 때까지 기다리길 바랍니다.
    // _.debounce 함수(또는 이와 유사한 _.throttle)에 대한
    // 자세한 내용을 보려면 https://lodash.com/docs#debounce 를 방문하세요.
    getAnswer: _.debounce(
      function () {
        if (this.question.indexOf('?') === -1) {
          this.answer = '질문에는 일반적으로 물음표가 포함 됩니다. ;-)'
          return
        }
        this.answer = '생각중...'
        var vm = this
        axios.get('https://yesno.wtf/api')
          .then(function (response) {
            vm.answer = _.capitalize(response.data.answer)
          })
          .catch(function (error) {
            vm.answer = '에러! API 요청에 오류가 있습니다. ' + error
          })
      },
      // 사용자가 입력을 기다리는 시간(밀리세컨드) 입니다.
      500
    )
  }
})
</script>
```



## Reference
- https://kr.vuejs.org/v2/guide/syntax.html