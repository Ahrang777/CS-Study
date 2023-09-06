# [DB] RDBMS와 NoSQL

## RDBMS

> 관계형 데이터베이스 관리 시스템.
> 속성(Attribute)과 값(Value)를 이용하여 데이터를 정의하고 저장 및 관리함

### 특징

- 테이블마다 스키마(Schema)를 정의한다.
  - 데이터 타입과 제약(Constraint)를 통해서 데이터의 정확성을 보장
- SQL문을 통해 요청을 처리한다.
  - 대표적으로 MySQL, Oracle DB가 존재
- 성능을 높이려면 하드웨어를 고성능으로 교체해야한다.
  - 즉, RDB는 성능 확장에 불리함
- 수직적 확장이 (Vertical Scaling) 가능하다
  - `수직적 확장`: 데이터베이스 서버의 성능을 향상시키는 것

### 장점

- 데이터의 분류, 정렬, 탐색 속도가 비교적 빠르다.
- SQL이라는 구조화된 질의를 통해 데이터를 다룰 수 있다.
- 작업의 완전성을 보장한다.

### 단점

- 반드시 스키마 규격에 맞춰서 데이터를 다뤄야 한다.
- 데이터 처리에 대한 부하가 발생하면 처리가 어렵다.

### RDBMS 사용이 권장되는 경우

- 관계를 맺은 데이터가 자주 변경되는 경우
- 변경될 여지가 없으며 명확한 스키마가 존재하는 경우

## NoSQL

> 비관계형 데이터베이스.
> 데이터와 테이블 간의 관계를 정의하지 않고, key와 value 값으로만 속성을 나타냄.

### 특징

- RDBMS와는 다르게 고정된 스키마와 JOIN이 존재하지 않는다.
  - 스키마 없이 동작하기 때문에 데이터가 추가 될 시에 구조에 대한 정의를 변경할 필요성이 사라진다. 따라서 각기 다른 데이터 타입을 가질 수 있다.
  - 각 테이블 간의 관계를 정의하지 않았기 때문에 JOIN 개념이 필요하지 않다.
- 대용량의 데이터를 저장할 수 있다.
- 분산형 구조를 가진다.
  - RDBMS와 같이 하나의 고성능 서버에 데이터를 저장하는 것이 아닌, 여러 대의 서버에 연결해 데이터를 저장하고 처리하는 구조로서 `수평적 확장`에 용이하다.
  - 분산형 구조를 통해 데이터를 여러 대의 서버로 분산해 저장할 수 있으며, 장애 발생 시 유연하게 대처할 수 있다.

### 장점

- 데이터 간의 관계를 정의하지 않는다.
- RDBMS 보다 복잡도가 떨어져, 대용량의 데이터를 저장 및 관리할 수 있다.
- 스키마가 정해져 있지 않아 데이터 저장이 비교적 자유롭다.
- 많은 양의 데이터를 저장 및 처리할 수 있다.

### 단점

- key 값에 대한 입, 출력만 지원한다.
- 스키마가 정해져 있지 않아 데이터에 대한 규격화가 되어 있지 않다.
- 데이터를 update하는데 비교적 느리다.

### NoSQL 사용이 권장되는 경우

- 정확한 데이터 구조를 알 수 없으며, 변경 및 확장이 가능한 경우
- 데이터의 읽기 행위가 대다수이며 변경 행위는 많지 않은 경우(=여러 데이터를 변경할 필요가 없는 경우)
- 데이터베이스를 막대한 데이터 양에 의해 수평적으로 확장해야 하는 경우