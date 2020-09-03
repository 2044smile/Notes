# 파비콘, 아이콘, 폰트, 반응형 태그 설정하기

## Viewport(반응형 태그)

```html
<meta name="viewport" content="width=device-width,initial-scale=1.0">
```

- 웹사이트가 반응형 웹 사이트다 라는 표시입니다.
- index.html 에 추가해주시면 됩니다.

## Favicon(파비콘)

```html
<link rel="shortcut icon" href="src/assets/favicon.ico" type="image/x-icon">
<link rel="icon" href="src/assets/favicon.ico" type="image/x-icon">
```

## FontAwesome

```html
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.13.0/css/all.min.css" rel="stylesheet">
```

- 아이콘 관련

## Google Font

```css
App.vue -> 강좌에서는 index.html 에 위치시킵니다.

<style>
@import url('https://fonts.googleapis.com/css2?family=Do+Hyeon&display=swap');
#app {
  font-family: 'Do Hyeon', sans-serif;
}
</style>
```

## Reference

- [w3schools](https://www.w3schools.com/css/css_rwd_viewport.asp)
- [favicon](https://www.favicon-generator.org/)
- [FontAwesome](https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css)
