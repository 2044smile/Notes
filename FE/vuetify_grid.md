## What is gird system
- Vuetify 는 12 구획으로 나누어진 그리드 시스템을 지원합니다. 그리드는 어플리케이션의 컨텐츠를 배열하는데 도움을 줍니다. 물론 CSS 를 조작하여 배치를 조정해도 됩니다만, 생산성 측면에서 이러한 시스템을 따르는 것이 유리합니다. 그리드 시스템은 5가지 유형의 매체 타입에 맞추어져 있습니다. (여기서 말하는 5가지 유형 매체 타입이란 웹, 스마트폰, TV, 테블릿 등등을 말하는 것 같습니다.)

### Use grid system
- 그리드 시스템을 사용하기 위해서는 아래의 세가지 컴포넌트를 알 필요가 있습니다.
1. v-container
2. v-layout
3. v-flex

위 컴포넌트들은 위에서 아래로 갈수록 하위 컴포넌트입니다.

#### v-container
- v-container는 중앙 중심의 페이지에 적용됩니다. 만약 전체 너비를 이용하고자 할 경우 fluid 속성(prop)을 전달해줍니다.

```html
<v-container fluid>
</v-container>
```

#### v-layout
- v-layout 컴포넌트는 각 섹션을 분리하는데 사용됩니다. 그리고 v-flex를 사용하기 위해 필수입니다.

#### v-flex
- CSS 의 플렉스는 엘리먼트의 크기나 위치를 쉽게 잡아두는 도구입니다. 레이아웃을 효과적으로 표현하기 위해 도입된 도구입니다.

### 레이아웃 잡기
```html
<div id="app">
  <v-app>
    <v-container>
      <v-layout column>
         <v-flex>
          <v-sheet>
            우리는 인생을 사는 이유를 깨우쳐야한다.
          </v-sheet>
          <v-btn :label="btnLabel"> {{ btnLabel }}</v-btn>
         </v-flex>
        <v-flex>
             <v-btn :label="btnLabel"> {{ btnLabel }}</v-btn>
         </v-flex>
        <v-flex>
             <v-btn :label="btnLabel"> {{ btnLabel }}</v-btn>
         </v-flex>
      </v-layout>
    </v-container>  
  </v-app>
</div>
```
- 아래 Reference 의 링크를 따라가보면 결과를 확인해볼 수 있습니다. v-layout 안에 v-flex 마다 본인의 세션을 갖고 관리할 수 있습니다.

### Reference
- https://code-machina.github.io/2019/02/17/Vuetify-Layout-Part-1.html
- [vuetify grid](https://codepen.io/code-machina,"link")
- [vuetify grid 최고 설명](https://chansbro.github.io/vue/vuetify_tutorial1,"link")
