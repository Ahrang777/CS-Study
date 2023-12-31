## 웹스토리지

### 웹 스토리지

- window 객체 안에 들어 있다.
- 5MB의 저장 용량을 갖는다.(모바일은 2.5MB, 부족하다면 50MB를 저장할 수 있는 IndexedDB)
- 요청 시 Headers에 전송하지 않는다.(쿠키의 CSFR, 트래픽 문제 해결)

### 로컬 스토리지

- 도메인/브라우저 별로 독립된 스토리지를 사용한다.
- 직접 삭제하지 않는 이상 유지된다.

### 세션 스토리지

- 탭 별로 독립된 스토리지를 사용한다.
- 탭 종료 시 스토리지가 삭제된다.

### 문제점

- XSS: 자바스크립트로 접근 가능
- 독립된 스토리지로 브라우저, 탭 간 공유가 불가하다.
- 만료 기간 설정이 불가하다.
- 동기적으로 실행해 메인 스레드를 블로킹할 수 있다.

### 웹 스토리지 보안 문제 해결 방안

- XSS: innerHTML, document.write 등을 사용하지 않는다. 사용자의 입력이 자바스크립트 코드로 실행될 수 있는 코드를 작성하지 않는다.
- innerHTML 사용 지양 XSS 보안 라이브러리를 사용한다.(sanitize-html, DOMPurify)
