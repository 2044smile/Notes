# Flux

- MVC 패턴의 복잡한 데이터 흐름 문제를 해결하는 개발 패턴 (단방향)
- Action -> Dispatcher -> Model -> View

1. Action: 화면에서 발생하는 이벤트 또는 사용자의 입력
2. Dispatcher: 데이터를 변경하는 방법, method
3. Model: 화면에 표시할 데이터, data
4. View: 사용자에게 비춰지는 화면

## MVC 패턴의 문제점

- 1개의 컨트롤러로 여러개의 Model 을 관리하는데 수 많은 Model 과 View 가 있고, 서로 데이터를 변경하는 작업이 수없이 이루어진다고 하였을 때 데이터의 추적이 어렵습니다.
