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
