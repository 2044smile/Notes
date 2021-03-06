## Parquet 이란
- Apache Spark 컬럼 기반 저장 포맷 Parquet
- 타다 내부에서 저장 포맷 변경 작업을 진행하였고 결과적으로 74%의 저장 용량 이득, 10~30 배의 처리 성능 이득을 얻었다.
- Parquet(나무조각을 붙여넣은 마룻바닥) 데이터를 나무조각처럼 차곡차곡 정리해서 저장한다는 의도이지 않을까
- 빅데이터 처리는 보통 많은 시간과 비용이 들어가므로 압축률을 높이거나, 데이터를 효율적으로 정리해서 처리하는 데이터의 크기를 1/2 혹은 1/3 으로 줄일 수 있다면 이는 매우 큰 이득입니다.

### 컬럼 기반 포맷의 장점
- 같은 종류의 데이터가 모여있으므로 압축률이 높습니다.
- 일부 컬럼만 읽어 들일 수 있어 처리량을 줄일 수 있습니다.
- 저장용량이 줄어든 것으로도 네트워크 I/O 가 줄어들기 때문에 처리 속도가 상당히 올라갑니다.
- **열 지향은 "읽기" 에 이점이 있고, 행 지향은 "업데이트" 에 이점이 있습니다.** 빅데이터 생태계에서 열 중심을 선호하는 이유이다.


[컬럼 기반 포맷과 로우 기반 포맷 비교 사진]('https://www.slideshare.net/larsgeorge/parquet-data-io-philadelphia-2013')



## Reference
- [타다 기술블로그]('http://engineering.vcnc.co.kr/2018/05/parquet-and-spark/')
- [열 지향 행 지향 차이점]('https://presmarymethuen.org/ko/dictionary/what-is-the-difference-between-a-column-oriented-and-a-row-oriented-database/')