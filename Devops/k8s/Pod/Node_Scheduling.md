# Pod (Node Scheduling)

## NodeSelector (권장)

- Key: Value 형태로 노드를 선택할 수 있습니다.
- 장점이자 단점인 것은 Key: Value 가 딱 맞는 곳에만 생성됩니다. 만약 맞는 라벨이 없다면 생성되지 않습니다.
ex) KR: az-1

## Node Affinity

- Key 만 설정해두면 해당 그룹핑에 스케쥴러를 통해서 자원이 많은 곳에 할당이되고, 해당 조건에 맞지 않는 키가 와도 자원이 남는 곳에 할당해주는 것을 옵션으로 컨트롤 할 수 있습니다.
- matchExpressions

## Pod Affinity

- Pod 가 같이 한 노드에 생성되어야 하는 경우에 사용합니다.

## Anti Affinity

- Master 가 죽으면 Slave 가 백업을 하는 상황일 경우 서로 다른 Node 에 위치시는 것 입니다.

## Toleration

- 노드에 할당이되려면 Toleration 이 달려있어야만 생성되는 경우

## Taint
