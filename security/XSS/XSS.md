# XSS

## XSS (Cross-Site Scripting)
> 권한 없는 사용자가 악의적인 용도로 웹 사이트에 스크립트를 삽입하는 공격 기법

- 다른 웹사이트와 정보를 교환하는 식으로 작동하므로 사이트 간 스크립팅이라 부른다.
- 웹 애플리케이션이 사용자로부터 입력 받을 값을 제대로 검사하지 않고 사용할 경우 나타난다.
- 공격에 성공하면 사이트에 접속한 사용자는 삽입된 코드를 실행하게 되어, 의도치 않은 행동을 수행시키거나 쿠키나 세션, 토큰 등의 민감한 정보를 탈취한다.
- 자바스크립트를 사용하여 공격하는 경우가 가장 많고, 사용자의 세션을 공격자의 서버로 전송해서 탈취하거나 악성코드가 있는 페이지로 리다이렉트 시키는 방식으로 공격이 주로 행해진다.
- 그 외에도 자바스크립트를 활용해서 내부 네트워크 포트스캔과 같은 공격도 가능하다.

##  XSS 공격 순서

<img src="https://github.com/Ahrang777/CS-Study/assets/72875528/93a3b795-2ca4-4c57-8df0-38358bbf8894" width="60%" height="50%"/>

1. 해커가 사전에 만든 웹페이지에 사용자가 브라우저로 엑세스를 시도한다.
2. XSS공격 link가 포함된 웹페이지가 브라우저에 표시한다.
3. 사용자가 link를 클릭한다.
4. 사용자가 느끼지 못하는 사이 취약한 사이트에 있는 해커의 스크립트에 엑세스 된다.
5. 사용자의 웹브라우저 상에서 해커의 스크립트가 실행된다.

## XSS 종류
### 1. Reflected XSS
- URL의 변수 부분처럼 스크립트 코드를 입력하는 동시에 결과가 바로 전해지는 공격기법
- 피싱 공격의 일부로 자주 사용되며 악용하기도, 차단하기도 쉽다.
- 공격자가 HTTP 요청에 악성 콘텐츠를 주입하면 그 결과가 사용자에게 반사되는 형태이다.
- 링크를 클릭하도록 피해자를 속이고, 유인해 세션을 하이재킹 할 수 있는 공격으로 피싱 공격에서 가장 많이 사용된다.

### 2. Stored XSS
- 가장 일반적인 XSS 공격 유형으로 가장 위험한 XSS 공격 유형이다.
- 사용자가 게시물을 열람 시, 공격자가 입력해놓은 악성 스크립트가 실행되어 사용자의 쿠키 정보가 유출되거나, 악성 스크립트가 기획한 공격에 당한다.
- 공격자가 웹 어플리케이션을 속여 데이터베이스에 악성코드를 저장하도록하는 수법으로 서버에 저장된 악성코드는 시스템 자체를 공격할 수 있으며, 사용자 상당 수 혹은 전체에 악성 코드를 전송할 수 있다.
- ex) 블로그 댓글에 악성코드를 게시하는 것

## XSS 대응 방안
1. 입력 값 제한
2. 입력 값 치환
3. 스크립트 영역에 출력 자제
    - 이벤트 핸들러 영역에 스크립트가 삽입되는 경우 보호 기법들을 우회할 수 있다.
    - 따라서 사용자의 입력을 출력하는 것을 최대한 자제해야 한다.
4. 라이브러리 이용
    - Anti XSS 라이브러리 이용

## XSS 공격을 방지하는 7계명
1. 허용된 위치가 아닌 곳에 신회할 수 없는 데이터가 들어가는 것을 허용하지 않는다.
2. 신뢰할 수 없는 데이터는 검증한다.
3. HTML 속성에 신뢰할 수 없는 데이터가 들어갈 수 없도록 한다.
4. 자바스크립트에 신뢰할 수 없는 값이 들어갈 수 없도록 한다.
5. CSS의 모든 신뢰할 수 없는 값에 대해서 검증한다.
6. URL 파라미터에 신뢰할 수 없는 값이 있는지 검증한다.
7. HTML 코드를 전체적으로 한번 더 검증한다.

## 참고

https://easymedia.net/Culture/EasyStory/?no=170&mode=view&IDX=1165&p=1