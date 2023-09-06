# DNS

## DNS (Domain Name System)

- 사람이 읽을 수 있는 도메인 이름(예: www.amazon.com)을 머신이 읽을 수 있는 IP 주소(예: 192.0.2.44)로 변환한다.

## 구성요소

1. 도메인 네임 스페이스(Domain Name Space)
2. 네임 서버(Name Server) = 권한 있는 DNS 서버
3. 리졸버(Resolver) = 권한 없는 DNS 서버

### 도메인 네임 스페이스

> DNS가 저장 관리하는 계층적 데이터베이스

<img src="https://github.com/Ahrang777/CS-Study/assets/72875528/a316a3b8-094d-4053-92b9-692a1547281f" width="60%" height="50%"/>

- 도메인 네임 스페이스는 최상위에 루트 DNS 서버가 존재하고 그 하위로 연결된 모든 노드가 연속해서 이어진 계층 구조로 되어있다.

#### 계층적 도메인 레벨(Hierarchical Domain Level)

- 도메인 네임 스페이스의 트리 구조는 최상위 레벨부터 순차적으로 계층적 소속 관계를 나타낸다.

#### FQDN(Fully Qualified Domain Name)

> 도메인의 전체 이름을 표기하는 방식

- 도메인 이름 : example.com
- 호스트 이름 : www
- FQDN : www.example.com

### 네임 서버

> Name Server, DNS Server

- 문자열로 표현된 도메인 이름을 실제 컴퓨터가 통신할 때 사용하는 IP 주소로 변환시키기 위해서는 도메인 네임 스페이스의 트리 구조에 대한 정보가 필요하다.
- 이러한 정보를 가지고 있는 서버를 네임 서버라고 한다.

1. Root DNS 서버

- ICANN이 직접 관리하는 절대 존엄 서버
- TLD DNS 서버 IP주소를 저장하고 안내하는 역할

2. Top-Level Domain(TLD) DNS 서버

- 도메인 등록 기관이 관리하는 서버
- SLD DNS 서버의 주소를 저장하고 안내하는 역할

3. Second-Level Domain(SLD) DNS 서버

- Authoritative DNS 서버라고도 한다.
- 실제 개인 도메인과 IP주소의 관계가 기록되는 서버

4. 권한 없는 DNS 서버

- 리졸버 서버, 리컬시브 서버, 리커서

#### 권한 있는 DNS 서버 vs 권한 없는 DNS 서버

1. 권한 있는 DNS 서버

- Root DNS 서버, Top-Level Domain(TLC) DNS 서버, Second-Level Domain(SLD) DNS 서버
- IP 주소와 도메인 이름을 매핑한다.

2. 권한 없는 DNS 서버

- 질의를 통해 IP 주소를 알아내거나 캐시한다.

### 리졸버

- 웹 브라우저와 같은 DNS 클라이언트의 요청을 네임 서버로 전달하고 네임 서버로부터 정보(도메인 이름, IP 주소)를 받아 클라이언트에게 제공하는 기능을 수행한다.

## 동작원리

<img src="https://github.com/Ahrang777/CS-Study/assets/72875528/9d8596ba-4bf9-4bc6-a919-b08ae2a133a9" width="80%" height="50%"/>

### DNS 조회의 8단계

1. 사용자가 웹 브라우저에 'example.com'을 입력하면, 쿼리가 인터넷으로 이동하고 DNS 재귀 확인자가 이를 수신한다.
2. 확인자가 DNS 루트 이름 서버(.)를 쿼리한다.
3. 루트 서버가 도메인에 대한 정보를 저장하는 최상위 도메인(TLD) DNS 서버(예: .com 또는 .net)의 주소로 확인자에 응답한다. example.com을 검색할 경우의 요청은 .com TLD를 가리킨다.
4. 확인자가 .com TLD에 요청한다.
5. TLD 서버가 도메인 이름 서버(example.com)의 IP주소로 응답한다.
6. 재귀 확인자가 도메인의 이름 서버로 쿼리를 보낸다.
7. example.com의 IP 주소가 이름 서버에서 확인자에게 반환된다.
8. DNS 확인자가 처음 요청한 도메인의 IP 주소로 웹 브라우저에 응답한다.

DNS 조회의 8단계를 거쳐 example.com의 IP 주소가 반환되면, 이제 브라우저가 웹 페이지를 요청할 수 있다.  
9. 브라우저가 IP 주소로 HTTP 요청을 보낸다.  
10. 해당 IP 서버가 브라우저에서 렌더링할 웹 페이지를 반환한다.

### DNS 확인자

- DNS 조회의 첫 번째 중단점이며, 최초 요청을 한 클라이언트 처리를 담당한다.

### DNS 쿼리

- 일반적인 DNS 조회에서는 세 가지 유형의 쿼리가 발생한다.

1. 재귀 쿼리

- 확인자가 레코드를 찾을 수 없는 경우, DNS 클라이언트는 DNS 서버가 요청한 자원 레코드 또는 오류 메시지를 사용하여 클라이언트에 응답하도록 요구한다.

2. 반복 쿼리

- DNS 클라이언트는 DNS 서버가 가능한 최상의 응답을 반환하도록 한다.
- 쿼리한 DNS 서버가 쿼리 이름과 일치하는 이름을 갖고 있지 않는 경우, 하위 수준의 도메인 네임스페이스에 대해 권한 있는 DNS 서버에 대한 참조를 반환한다.
- 그러면 DNS 클라이언트가 참조 주소를 쿼리한다.
- 이 프로세스는 오류 또는 제한 시간 초과가 발생할 때까지 추가 DNS 서버가 쿼리 체임을 중단한 상태로 계속된다.

3. 비재귀 쿼리

- DNS 확인자 클라이언트의 쿼리를 받은 DNS 서버가 해당 레코드에 대한 권한이 있거나 캐시 내부에 해당 레코드를 갖고 있고, DNS 서버가 액세스 권한을 갖고 있는 레코드를 쿼리할 때 발생합니다.
- 일반적으로, DNS 서버는 추가 대역폭 소비 및 업스트림 서버의 부하를 방지하기 위해 DNS 레코드를 캐시한다.

## DNS 서비스 유형

1. 신뢰할 수 있는 DNS

- 개발자가 퍼블릭 DNS 이름을 관리하는 데 사용하는 업데이트 메커니즘 제공
- 이 메커니즘을 통해 DNS 시스템은 DNS 쿼리에 응답하고 도메인 이름을 IP 주소로 변환한다.
- 신뢰할 수 있는 DNS는 도메인에 대해 최종 권한이 있으며 재귀적 DNS 서버에 IP 주소 정보가 담긴 답을 제공할 책임이 있다.

2. 재귀적 DNS

- 클라이언트는 신뢰할 수 있는 DNS 서비스에 직접 쿼리를 수행하지 않는다.
- 대신 해석기 또는 재귀적 DNS 서비스라고 알려진 다른 유형의 DNS 서비스에 연결하는 경우가 일반적이다.
- DNS 레코드는 소유하고 있지 않지만 사용자를 대신해서 DNS 정보를 가져올 수 있는 중간자의 역할을 한다.
- 재귀적 DNS가 일정 기간 캐시된 또는 저장된 DNS 참조를 가지고 있는 경우, 소스 또는 IP 정보를 제공하여 DNS 쿼리에 답을 한다.
- 그렇지 않다면, 해당 정보를 찾기 위해 쿼리를 하나 이상의 신뢰할 수 있는 DNS 서버에 전달한다.

## DNS 캐싱

- 캐싱의 목적 : 데이터를 임시 저장하여 데이터 요청에 대해 성능과 신뢰성을 높이는 것
- DNS 캐싱은 요청하는 클라이언트와 가까운 곳에 데이터를 저장함으로써 DNS 쿼리를 조기에 확인할 수 있고 DNS 조회 체인의 추가 쿼리를 피할 수 있으므로, 로드 시간이 향상되고 대역폭/CPU 소비가 줄어든다.
- DNS 데이터는 다양한 위치에 캐시될 수 있으며, 각 위치는 TTL(Time-To-Live)에 의해 정의된 설저 시간 동안 DNS 레코드를 저장한다.

1. 브라우저 DNS 캐싱
2. 운영체제 수준 DNS 캐싱

## 참고

https://www.cloudflare.com/ko-kr/learning/dns/what-is-dns/  
https://hanamon.kr/dns%EB%9E%80-%EB%8F%84%EB%A9%94%EC%9D%B8-%EB%84%A4%EC%9E%84-%EC%8B%9C%EC%8A%A4%ED%85%9C-%EA%B0%9C%EB%85%90%EB%B6%80%ED%84%B0-%EC%9E%91%EB%8F%99-%EB%B0%A9%EC%8B%9D%EA%B9%8C%EC%A7%80/  
https://aws.amazon.com/ko/route53/what-is-dns/