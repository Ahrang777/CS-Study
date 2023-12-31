# MVC

## 개념

![Untitled (2)](https://github.com/RIN-1011/RIN-1011/assets/60701386/ef83d9fe-0b87-46af-8f42-923a767a4c24)

- MVC란 **M**odel-**V**iew-**C**ontroller의 약자로 애플리케이션을 세 가지 역할로 구분한 개발 방법론
- MVC는 소프트웨어가 서비스하는 방식에 대한 패턴을 지칭한다

## MVC 디자인 패턴 흐름

![Untitled (3)](https://github.com/RIN-1011/RIN-1011/assets/60701386/90563d68-80c3-4ab5-9f90-6f3884a45318)

- 위 그림처럼 사용자가 Controller를 조작하면 Controller는 Model을 통해 데이터를 가져오고 그 데이터를 바탕으로 View를 통해 시각적 표현을 제어하여 사용자에게 전달하게 된다.

### Model (모델)

- Model은 Data와 애플리케이션이 무엇을 할 것인지를 정의하는 부분으로 내부 비즈니스 로직을 처리하기 위한 역할을 수행한다.
- 즉, 모델은 컨트롤러가 호출을 하면 DB와 연동하여 사용자의 입출력 데이터를 다루는 일과 같은 데이터와 연관된 비즈니스 로직을 처리하는 역할을 한다.
- 데이터 추출(조회), 저장, 삭제, 업데이트(수정) 등의 역할을 수행한다.

**모델의 규칙**

- 사용자가 편집하길 원하는 모든 데이터를 가지고 있어야만 함
- 뷰나 컨트롤러에 대해서 어떠한 정보도 알지 말아야 함
- 변경이 일어나면, 변경 통지에 대한 처리방법을 구현해야 함
    - Model의 속성 중 텍스트 정보가 변경되면, 이벤트를 발생시켜 누군가에게 전달해야 하며, 누군가 Model을 변경하도록 요청하는 이벤트를 보냈을 때 이를 수신할 수 있는 처리 방법을 구현해야 한다. 이는 Model이 변경되는 방법을 다른 구성 요소에 알려주게 되는 방법이다.

### View (뷰)

- View는 사용자에게 보여주는 화면(UI)이 해당된다.
- 사용자와 상호작용을 하며 컨트롤러로부터 받은 모델의 결과값을 사용자에게 화면으로 출력하는 일을 한다.
- MVC에서는 여러 개의 View가 존재할 수 있다.
- Model에서 받은 데이터는 별도로 저장하지 않는다.

**뷰의 규칙**

- 모델이 가지고 있는 정보를 따로 저장해서는 안됨
- 모델이나 컨트롤러와 같이 다른 구성 요소를 몰라야 함
- 변경이 일어나면, 변경 통지에 대한 처리방법을 구현해야 함
    - Model과 같이 변경이 일어났을 때 이에 누군가에게 변경을 알려줘야 하는 방법을 구현해야 한다. View에서는 화면에서 사용자가 화면에 표시된 내용을 변경하게 되면 이를 Model에게 전달해서, Model을 변경하기 위해 변경 통지를 구현한다.

### ****Controller (컨트롤러)****

- Controller는 Model과 View 사이를 이어주는 인터페이스 역할을 한다.
- 즉, Model이 데이터를 어떻게 처리할지 알려주는 역할을 한다.
- 사용자로부터 View에 요청이 있으면 Controller는 해당 업무를 수행하는 Model을 호출하고 Model이 업무를 모두 수행하면 다시 결과를 View에 전달하는 역할을 한다.

**컨트롤러의 규칙**

- 모델이나 뷰에 대해서 알고 있어야 함
    - Model이나 View는 서로의 존재를 모르고, 변경을 외부로 알리고, 수신하는 방법만 가지고 있는데, 이를 Controller가 중재하기 위해 Model과 그에 관련된 View에 대해서 알고 있어야 한다.
- 모델이나 뷰의 변경을 모니터링해야 함
    - Model이나 View의 변경을 통지받으면, 이를 해석해서 각각의 구성 요소에 통지를 해야 한다.

## MVC 패턴 방식 (Model 1, Model 2)

- 모델 1 방식 : JSP에서 출력과 로직을 전부 처리
- 모델 2 방식 : JSP에서 출력만 처리

### Model 1

![Untitled (4)](https://github.com/RIN-1011/RIN-1011/assets/60701386/b9ff614f-facd-4d94-b04e-71b564fd87d1)

- 모델 1 방식은 Controller 영역에 View 영역을 같이 구현하는 방식이며, 사용자의 요청을 JSP가 전부 처리한다. 요청을 받은 JSP는 JavaBean Service Class를 사용하여 웹브라우저 사용자가 요청한 작업을 처리하고 그 결과를 출력한다.

![Untitled (5)](https://github.com/RIN-1011/RIN-1011/assets/60701386/a79a23d3-ba83-4968-a35f-ca31db444924)

### Model 2

![Untitled (6)](https://github.com/RIN-1011/RIN-1011/assets/60701386/8a75c484-5b7d-4da7-abf1-16371203b7bb)

- 모델 2 방식은 웹브라우저 사용자의 요청을 서블릿이 받고 서블릿은 해당 요청으로 View로 보여줄 것인지 Model로 보낼 것인지를 판단하여 전송한다. 또한 모델 2 방식의 경우 HTML 소스와 JAVA 소스를 분리해놓았기 때문에 모델 1 방식에 비해 확장시키기도 쉽고 유지보수 또한 쉽다.

### Model 1 vs Model 2

|  | Model 1 | Model 2 |
| :---: | --- | --- |
| 장점 | 빠르고 쉽게 개발 가능 | 디자이너와 개발자의 분업이 가능하며 유지보수 및 확장이 쉬움 |
| 단점 | JSP파일이 너무 비대해지며 Controller와 View가 혼재하므로 향후 유지보수에 어려움 | 설계가 어려우며 개발 난이도가 높음 |

→ Model 1 방식으로 웹서비스를 개발하는 사례는 백엔드와 프론트엔드의 역할 분담이 모호해져 협업이 쉽지 않으며 실제 서비스들 중에서 거의 없다고 봐도 무방

## 장점

- 비즈니스 로직과 UI 로직을 분리하여 유지보수를 독립적으로 수행 가능
    - 각 구성요소들을 독립시켜 협업을 할 때 맡은 부분의 개발에만 집중할 수 있어 개발의 효율성을 높여줌
- Model과 View가 다른 컴포넌트들에 종속되지 않아 애플리케이션의 확장성, 유연성에 유리함
- 기능별로 코드를 분리하여 하나의 파일에 코드가 모이는 것을 방지하여 가독성과 코드의 재사용이 증가함

## 한계점

![Untitled (7)](https://github.com/RIN-1011/RIN-1011/assets/60701386/6f7cf389-a743-4cf2-ab93-5da687e42932)

- MVC 패턴에서 View는 Controller에 연결되어 화면을 구성하는 단위 요소이므로 다수의 View를 가질 수 있다. 그리고 Model은 Controller를 통해서 View와 연결되지만, Controller에 의해서 하나의 View에 연결될 수 있는 Model도 여러 개가 될 수 있어 View와 Model이 서로 의존성을 띄게 된다. 즉, Controller에 다수의 Model과 View가 복잡하게 연결되어 있는 상황이 발생할 수 도 있다.
- View와 Model의 높은 의존성은 애플리케이션이 커질 수록 복잡해지고 유지보수가 어렵게 만들 수 있다.
    - 이를 보완하기 위해 MVP, MVVM, Flux, Redux등의 다양한 패턴들이 생겨남

## 참고

[https://velog.io/@seongwon97/MVC-패턴이란](https://velog.io/@seongwon97/MVC-%ED%8C%A8%ED%84%B4%EC%9D%B4%EB%9E%80)

https://cocoon1787.tistory.com/733

https://m.blog.naver.com/islove8587/220363245916

https://www.stevy.dev/react-state-management-guide/
