# 패스워드 암호화

## 암호화 종류

![Untitled (1)](https://github.com/RIN-1011/RIN-1011/assets/60701386/f4f2ca7f-083f-46a9-be3a-d027e94b2ef2)

## 양방향 암호화

![Untitled (2)](https://github.com/RIN-1011/RIN-1011/assets/60701386/ea444609-af40-45aa-8903-d1e86c3f520f)

### 개념

- 양방향 암호화는 암호화된 암호문을 복호화 할 수 있는 알고리즘을 의미한다.

### 종류

|  | 설명 | 장점 | 단점 | 대표 알고리즘 |
| --- | --- | --- | --- | --- |
| 대칭키(비공개키) | 암호화, 복호화 시 모두 동일한 키를 사용. 따라서 키 비공개 | 속도가 빠르다 | 키 배송 위험성 존재하여 송신 측에서 수신측에 암호 키를 전달하는 과정에서 노출우려가 있다. | DES, 3DES, AES, SEED, ARIA |
| 비대칭키(공개키) | 암호화, 복호화에 서로 다른 키를 사용. 하나의 키 공개키로 사용. | 키 배송의 문제를 근본적으로 차단하여 안전성이 높다. | 대칭키(비공개키)방식에 비해서 느리다. | RSA |

## 단방향 암호화

![Untitled (3)](https://github.com/RIN-1011/RIN-1011/assets/60701386/df46167b-8ab5-46fe-a9cb-5aad159da909)

### 개념

- 단방향 암호화는 암호화는 수행하지만 절대로 복호화가 불가능한 알고리즘을 의미한다.
- 수학적 연산에 의해 원본 데이터를 매핑시켜 완전히 다른 암호화된 데이터로 변환시키는 것을 해시라고 하며, 해시에 의해 암호화된 데이터를 **다이제스트**라고 한다.
- 예시
    
    ![Untitled (4)](https://github.com/RIN-1011/RIN-1011/assets/60701386/c8424f87-a295-4958-9346-1a2963e423f2)

    - 원본 메시지 123456 을 해시 함수에 돌려서 다이제스트인 fs32a3xzz0 을 생성하고 해당 데이터를 DB 에 저장하는 것이다. 이렇게 저장된 다이제스트는 설령 DB가 털린다 하더라도 fs32a3xzz0 은 단방향으로 해싱 된 문자라 복호화 할 수가 없는 것이다. 또한 의미를 파악할 수도 없다.

### 문제점

1. **동일한 메세지는 동일한 다이제스트를 갖는다.**
    1. 앞서 위의 123456 을 SHA-256 을 통해 다이제스트를 얻었다. 분명 123456 의 다이제스트는 원래의 password 인 123456 을 유추하기 어렵다. 그러나 123456 에 대한 다이제스트는 항상 같은 값을 얻는다는 것, 즉 값이 변하지 않는 것이 큰 문제점이다.
    2. 따라서 해커들이 여러 값들을 대입해보면서 얻었던 다이제스트들을 모아놓은 리스트에서 원문을 찾아 정보를 탈취한다. 이러한 다이제스트들의 테이블을 **레인보우 테이블**이라고 한다.
2. **무차별 대입 공격 (브루트포스)**
    1. 해시 함수의 경우 원래 빠른 데이터 검색을 위한 목적으로 설계된 것이다. 그렇다보니 해시 함수를 써도 원문의 다이제스트는 금방 얻어진다. 바로 이 점이 문제점인데, 우리가 다이제스트를 빠르게 얻을 수 있는 것과 동일하게 해커도 똑같이 빠르게 값을 얻을 수 있다는 것이다. 즉, 해커는 무작위의 데이터들을 계속 대입해보면서 얻은 다이제스트와 해킹할 대상의 다이제스트를 계속 비교를 해보는 것이다. 이런 방식으로 패스워드를 추측하면 패스워드가 충분히 길거나 복잡하지 않은 경우에는 그리 긴 시간이 걸리지 않는다. 그리고 대부분 사용자의 패스워드는 길거나 복잡하지 않을 뿐 아니라, 동일한 패스워드를 사용하는 경우도 많다.
    2. 따라서 해시 함수의 빠른 처리 속도는 사용자들보다 공격자들에게 더 큰 편의성을 제공하게 된다.

### 보완

1. **키 스트레칭 (key stretching)**
    
    ![Untitled (5)](https://github.com/RIN-1011/RIN-1011/assets/60701386/75dcb602-bd1d-4334-9e14-7949eb88e7f6)

- 여러 단계의 해시 함수를 적용하여 다이제스트를 생성하는 과정
- 예시
    
    예로들어 SHA-256 을 사용한다고 가정할 때, 123456 이 입력되었다면 123456 의 다이제스트는 아래와 같았다.<br>
    **`8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92`**
    
    이 다이제스트를 한 번 더 SHA-256 에 돌리는 것이다. 그러면 아래와 같은 값이 나온다.<br>
    **`49dc52e6bf2abe5ef6e2bb5b0f1ee2d765b922ae6cc8b95d39dc06c21c848f8c`**
    
    따라서 입력한 패스워드를 동일한 횟수만큼 해시해야만 입력한 패스워드의 일치 여부를 확인할 수 있다.
    
    ---
    
    ⇒ 해시 함수를 여러번 돌리는 만큼 최종 다이제스트를 얻는데 시간이 소요되며 이는 브루트포스를 최대한 무력화 하기 위한 방법이다.
    

2. **솔팅 (Salting)**

![Untitled (6)](https://github.com/RIN-1011/RIN-1011/assets/60701386/f79d5336-59c4-4e6f-8876-f749f0588e30)

- **솔트(salt)** : 단방향 해시 함수에서 다이제스트를 생성할 때 추가되는 바이트 단위의 임의의 문자열
- **솔팅** : 이 원본 메시지에 문자열을 추가하여 다이제스트를 생성하는 것
- 예시
    
    사용자1과 사용자2가 123456 이라는 같은 password 를 사용하고 있다. 
    
    사용자1 솔트 값 : sffs13osz043opq9dsfdkj32<br>
    사용자2 솔트 값 : osela31dif3298hcwaw8s301
    
    사용자1이 해시함수를 돌리기 전에 솔팅된 문자열은 123456sffs13osz043opq9dsfdkj32 이고, SHA-256 에 돌리면 다음과 같은 값을 얻을 수 있다.<br>
    **`343099b2867417f1b60462a8c70aa9dc33f4b1cec287fdb22e9fcf9b999ee3ce`**
    
    사용자2의 경우 해시함수를 돌리기 전 솔팅된 문자열은 123456osela31dif3298hcwaw8s301 이다. 이를 SHA-256 을 사용하여 해싱 하면 다음과 같은 값을 얻는다.<br>
    **`725c8c66c181855dd578961d90b2a051a250b232ede85a7ab5da5d0d4586d135`**
    
    즉, 같은 패스워드를 사용하더라도 salting 된 문자열은 서로 다르기 때문에 각 사용자의 다이제스트는 서로 다른 값으로 저장될 것이다. 해커가 123456 의 다이제스트를 갖고 있다고 하더라도 레인보우 테이블에서 비교하기 어렵게 만드는 것이다.
    
    ---

    ⇒ 사용자마다 다른 Salt 를 사용한다면 설령 같은 비밀번호더라도 다이제스트의 값은 다르다. 따라서 해커가 다이제스트를 알아낸다 하더라도 password를 알아내기 어렵게 하는 방법이다.

## 참고

https://junho94.tistory.com/30

https://st-lab.tistory.com/100

https://junho94.tistory.com/30

[https://velog.io/@kho5420/bcrypt-jwt-양방향-암호화-단방향-암호화](https://velog.io/@kho5420/bcrypt-jwt-%EC%96%91%EB%B0%A9%ED%96%A5-%EC%95%94%ED%98%B8%ED%99%94-%EB%8B%A8%EB%B0%A9%ED%96%A5-%EC%95%94%ED%98%B8%ED%99%94)

https://javaplant.tistory.com/26
