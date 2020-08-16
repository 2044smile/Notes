# Slots

## What is Slot

- Vue.js 에서 slot 은 부모 컴포넌트의 template 에 있는 일부 노드를 자식 컴포넌트로 전달해주는 것이라 할 수 있습니다.

## Example

- 자식컴포넌트에서 선언한 slot name="header" 부분에 부모컴포넌트에서 template v-slot:header 로 데이터를 삽입할 수 있다.
- 자식컴포넌트 <slot name="<name>">
- 부모컴포넌트 <template v-slot:"<name>">blah blah~</template>

**자식 컴포넌트**
```html
<div class=""container>
    <header>
        <slot name="header"></slot>
    </header>
    <main>
        <slot></slot>
    </main>
    <footer>
        <slot name="footer"></slot>
    </footer>
</div>
```

**부모 컴포넌트**
```html
<base-layout>
    <template v-slot:header>
        <h1>Here might be a page title</h1>
    </template>
    
    <p>A paragraph for the main content.</p>
    <p>And another one.</p>

    <template v-slot:footer>
        <p>Here's some contact info</p>
    </template>
</base-layout>
```


## Reference
- https://kr.vuejs.org/v2/guide/components-slots.html