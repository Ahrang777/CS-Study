## 정리

### **쿠키**

- **저장 위치:** 클라이언트 측 (브라우저 내부)
- **용도:** 브라우저와 서버 간의 데이터 교환, 상태 유지
- **지속성:** 만료 날짜 또는 기간을 설정하여 일정 기간 동안 유지 가능
- **용량 제한:** 보통 4KB로 제한되어 작은 데이터 저장에 적합
- **전송:** 모든 HTTP 요청에 쿠키 데이터가 포함되어 서버로 전송됨
- **보안:** 보안 취약성이 있으며, 중요한 정보를 저장하기에는 적절하지 않을 수 있음
- **사용 예시**: n일 동안 보지 않기, 자동 로그인

### **세션**

- **저장 위치:** 서버 측 (웹 서버의 메모리 또는 데이터베이스)
- **용도:** 사용자의 상태 및 데이터 유지, 사용자 인증
- **지속성:** 일정 시간 동안 유지되며, 사용자 활동이 없을 경우 만료될 수 있음
- **용량 제한:** 서버 용량에 따라 다르며, 일반적으로 더 많은 데이터 저장 가능
- **전송:** 세션 ID만 쿠키로 클라이언트에 저장되고, 실제 데이터는 서버에 저장되므로 상대적으로 안전함
- **보안:** 클라이언트 측에서 직접 수정할 수 없으며, 중요한 데이터 저장에 적합
- **사용 예시**: 쇼핑몰 장바구니

### **웹 스토리지**

- **저장 위치:** 클라이언트 측 (브라우저 내부)
- **용도:** 클라이언트 측에서 임시 데이터 유지, 브라우저 창 또는 탭이 열려 있는 동안에만 유지
- **지속성:** 브라우저 세션이 유지되는 동안 데이터 저장, 브라우저 종료 시 삭제
- **용량 제한:** 쿠키와 유사한 크기로 제한됨 (보통 5MB)
- **전송:** 서버로 자동 전송되지 않음, 클라이언트 측에서만 사용
- **보안:** 상대적으로 취약하며, 중요한 데이터 저장에는 부적절할 수 있음
- **사용 예시**: 사용자 설정 저장, 글 임시 저장 / 이전 페이지 저장, 이전 스크롤 위치 저장

## 참고

- [https://racoonlotty.tistory.com/entry/쿠키와-세션-그리고-로컬-스토리지와-세션-스토리지](https://racoonlotty.tistory.com/entry/%EC%BF%A0%ED%82%A4%EC%99%80-%EC%84%B8%EC%85%98-%EA%B7%B8%EB%A6%AC%EA%B3%A0-%EB%A1%9C%EC%BB%AC-%EC%8A%A4%ED%86%A0%EB%A6%AC%EC%A7%80%EC%99%80-%EC%84%B8%EC%85%98-%EC%8A%A4%ED%86%A0%EB%A6%AC%EC%A7%80)
- https://interconnection.tistory.com/74
- https://thecodinglog.github.io/web/2020/08/11/what-is-session.html
- [https://velog.io/@hyun6ik/세션-동작-방식](https://velog.io/@hyun6ik/%EC%84%B8%EC%85%98-%EB%8F%99%EC%9E%91-%EB%B0%A9%EC%8B%9D)
