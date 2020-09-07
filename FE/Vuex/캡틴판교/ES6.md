# ES6 for Vue.js

- Const & Let, Arrow Function, Enhanced Object Literals, Modules 학습

## Babel

- 구 버전 브라우저 중에서는 ES6의 기능을 지원하지 않는 브라우저가 있으므로 transpiling 이 필요
- ES6의 문법을 각 브라우저의 호환 가능한 ES5로 변환하는 컴파일러

## ES6 란

- ES6(ECMAScript 2015)
- 최신 Front-End Framework 인 React, Angular, Vue 에서 권고하는 언어 형식
- 문법이 간결해서 익숙해지면 생산성이 높아진다.

### const & let (새로운 변수 선언 방식)

- 블록 단위 { } 로 변수의 범위가 제한되었음
- `const`: 한번 선언한 값에 대해서 변경할 수 없음(상수 개념)
- `let`: 한번 선언한 값에 대해서 다시 선언할 수 없음

### Arrow Function - 화살표 함수

- 함수를 정의할 때 function 이라는 키워드를 사용하지 않고 => 로 대체
- 흔히 사용하는 콜백 함수의 문법을 간결화

```javascript
// ES5
var sum = function(a, b) {
    return a + b;
}

// ES6
var sum = (a, b) => {
    return a + b;
}

sum(10, 20)
```

### Enhanced Object Literals - 향상된 객체 리터럴

- 객체의 속성을 메서드로 사용할 때 function 예약어를 생략하고 생성 가능

```javascript
var dictionary = {
    words: 100,
    // ES5
    lookup: function() {
        console.log("find words");
    },
    // ES6
    lookup() {
        console.log("find words");
    }
};
```

- 객체의 속성명(Key)과 값(Value) 명이 동일할 때 아래와 같이 축약이 가능합니다.

```javascript
let figures = 10;
var dictionary = {
    fingures // figures: figures
};
```

### Modeules - 자바스크립트 모듈화 방법

- 자바스크립트 모듈 로더 라이브러리(AMD, Commons JS) 기능을 js 언어 자체에서 지원
- 호출되기 전까지는 코드 실행과 동작을 하지 않는 특징이 있음

```javascript
// libs/math.js
export function sum(x, y) {
    return x + y;
}
export var pi = 3.141593;

// main.js
import {sum} from 'libs/math.js';
sum(1, 2);
```

## Reference

[Babel](https://babeljs.io/)
