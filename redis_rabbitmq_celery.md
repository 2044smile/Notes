## Celery (Worker)

* Celery 는 Python 으로 작성된 분산 메시지 전달을 기반으로 한 비동기 작업 큐로, Worker 의 한 종류다.
* 별도로 실행 중인 Worker Process 가 Broker 로 부터 Message 를 전달받아 작업을 대신 수행해주는 라이브러리다.

### Flow
* 요청을 받은 뷰에서는 Broker 에게 해당 작업 실행을 위임하고 각 작업을 구분할 수 있는 Task ID 를 발급받게 된다. 해당 작업은 Broker 가 놀고 있는 Worker 에 넘겨서 Worker 가 비동기로 수행하도록 한다.
* 

## Reference
* https://velog.io/@jisoo1170/Redis-RabbitMQ-%EC%B0%A8%EC%9D%B4%EC%A0%90%EC%9D%84-%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90