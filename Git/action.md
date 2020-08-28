# Git Action

## release

```yaml
name: release

on:
  release:
    types: [published]

jobs:
  release:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2

    blahblah
```

- 타입에는 다양한 옵션이 존재합니다. ex) [published, created, edited, . . .]

- 릴리즈를 생성할 때는 Tag 를 먼저 Push 하고 해당 태그를 클릭하여 create release 를 생성하는 것이 좋습니다. (태그 없이 릴리즈를 생성하게되면 동작하지 않음)

## Reference

- [GitHub Docs]('https://docs.github.com/en/actions/reference/events-that-trigger-workflows#release')
- [Action Hello World Tutorial]('https://lab.github.com/githubtraining/github-actions:-hello-world')
- [어쩐지 오늘은님 블로그]('https://zzsza.github.io/development/2020/06/06/github-action/')