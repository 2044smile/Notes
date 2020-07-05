# Do It! Vue.js 입문 

## 전역컴포넌트, 지역컴포넌트
### 전역컴포넌트

- 전역 컴포넌트는 뷰 라이브러리를 로딩하고 나면 접근 가능한 Vue 변수를 이용하여 등록합니다.
전역 컴포넌트를 모든 인스턴스에 등록하려면 Vue 생성자에서 .component()를 호출하여 수행하면 됩니다.
```js
Vue.component('컴포넌트 이름', {
    // 컴포넌트 내용
})
```
```html
<html>
    <head>
        <title>Hello Vue Component</title>
    </head>
    <body>
    <div id="app">
        <button>컴포넌트 등록</button>
        <my-component></my-component>
    </div>

    <script>
    Vue.component('my-component', {
        template: '<div>전역컴포넌트등록완료</div>'    
    });
    new Vue({
        el: '#app'
    })
    </script>
    </body>
</html>
```

### 지역 컴포넌트
- 지역 컴포넌트 등록은 전역 컴포넌트 등록과는 다르게 인스턴스에 components 속성을 추가하고
등록할 컴포넌트 이름과 내용을 정의하면 됩니다.

```js
new Vue({
    components: {
        '컴포넌트 이름': '컴포넌트 내용'
    }
})

===========================================

var cmp = {
    template: '<div>지역 컴포넌트 등록</div>'
};

new Vue({
    el: '#app',
    components: {
        'my-local-component': cmp
    }
});

===========================================

<html>
  <head>
    <title>Vue Local and Global Components</title>
  </head>
  <body>
    <div id="app">
      <h3>첫 번째 인스턴스 영역</h3>
      <my-global-component></my-global-component>
      <my-local-component></my-local-component>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/vue@2.5.2/dist/vue.js"></script>
    <script>
      // 전역 컴포넌트 등록
      Vue.component('my-global-component', {
        template: '<div>전역 컴포넌트 입니다.</div>'
      });

      // 지역 컴포넌트 내용
      var cmp = {
        template: '<div>지역 컴포넌트 입니다.</div>'
      };

      new Vue({
        el: '#app',
        // 지역 컴포넌트 등록
        components: {
          'my-local-component': cmp
        }
      });
    </script>
  </body>
</html>
```

### 지역, 전역 컴포넌트의 차이점
- 정말 간단하게는 유효범위에 따라 차이가 있습니다.
- 실제 서비스에서는 지역 컴포넌트를 주로 많이 사용합니다.
- 전역 컴포넌트는 플러그인이나 라이브러리를 사용할 때 사용합니다.


### 상 하위 컴포넌트 관계
- 컴포넌트는 각각 고유한 유효 범위를 갖고 있기 때문에 직접 다른 컴포넌트의 값을 참조할 수 없습니다.
따라서 뷰 프레임워크 자체에서 정의한 컴포넌트 데이터 전달 방법을 따라야 합니다.
- 가장 기본적인 데이터 전달 방법은 바로 상위(부모) - 하위(자식) 컴포넌트 간의 데이터 전달 방법입니다.

#### props!!
- 상위에서 하위로는 props라는 특별한 속성을 전달합니다. 그리고 하위에서 상위로는 기본적으로 이벤트만 전달($emit)할 수 있습니다.

#### props 속성
- props는 상위 컴포넌트에서 하위 컴포넌트로 데이터를 전달할 때 사용하는 속성입니다.
```js
Vue.component('child-component', {
    props: ['props 속성 이름']
})
```
- 그런 다음 상위 컴포넌트의 HTML 코드에 등록된 child-component 컴포넌트 태그에 v-bind 속성을 추가합니다.
```html
<child-component v-bind:props 속성 이름="상위 컴포넌트의 data 속성"></child-component>
```
- **v-bind 속성의 왼쪽 값으로 하위 컴포넌트에서 정의한 props 속성을 넣고, 오른쪽 값으로 하위 컴포넌트에 전달할 상위 컴포넌트의 data 속성을 지정합니다.**

#### 예제
```html
<div id="app">
    <child-compoent v-bind:propsdata="message"></child-compoent>
</div>
```
```js
Vue.component('child-component', {
    props: ['propsdata'],
    template: '<p>{{ propsdata }}</p>',
});
new Vue({
    el: '#app',
    data: {
        message: 'Hello Vue!' // 상위의 message 속성
    }
});
```

- 예제 코드에서는 child-component를 전역으로 등록한 것 이외에 딱히 상위 컴포넌트를 지정하지 않았습니다.
그럼에도 불구하고 뷰 인스턴스 안에 마치 상위 컴포넌트가 존재하는 것처럼 하위 컴포넌트로 props를 내려보냈습니다.
- 그 이유는 컴포넌트를 등록함과 동시에 뷰 인스턴스 자체가 상위 컴포넌트가 되기 때문입니다.

### 하위에서 상위 컴포넌트로 이벤트 전달하기
#### 이벤트 발생과 수신
- 하위 컴포넌트에서 상위 컴포넌트로의 통신은 어떻게할까?
- 이벤트를 발생시켜(event emit) 상위 컴포넌트에 신호를 보내면 됩니다.
- 상위 컴포넌트에서 하위 컴포넌트의 특정 이벤트가 발생하기를 기다리고 있다가 하위 컴포넌트에서 특정 이벤트가 발생하면
상위 컴포넌트에서 해당 이벤트를 수신하여 상위 컴포넌트의 메서드를 호출하는 것 입니다.

```js
//이벤트 발생
this.$emit('eventName')

//이벤트 수신
<child-component v-on:eventName="상위 컴포넌트의 메서드명"></child-component>
```

- $emit()을 호출하면 괄호 안에 정의된 이벤트가 발생합니다. 그리고 일반적으로 $emit()을 호출하는 위치는
하위 컴포넌트의 특정 메서드 내부입니다. 따라서 $emit()을 호출할 때 사용하는 this는 하위 컴포넌트를 가리킵니다.