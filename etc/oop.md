`Imperative and Procedural Programming`
절차지향적 프로그래밍
정의된 순서대로 절차적으로 함수를 하나씩 호출
단점이 많다
함수가 얽혀있어 하나 수정시 사이드이펙트 발생확률이 높음
가독성이 낮다
유지보수/확장이 어렵다


`Object Oriented Programming`
객체지향 프로그래밍
객체들끼리 서로 의사소통 하도록 코딩
서로 관련있는 데이터와 함수를 오브젝트로 정의.
-productivity, higher-quality, faster
object(data, function)

MediaPlayer - music data, play/stop 함수
학생, 은행…다양한 객체
Error Exception Event 도 다 오브젝트로 만들고 관리할 수
‘명사’로 이름
데이터 - fields, property
Function - methods 
대게는 클래스로 정의

:오브젝트의 생김새를 묘사(청사진)
Class (붕어빵 틀) -> 데이터 넣어서 -> 붕어빵(object)
-template
-declare once
-no data in 

Object
-instance of a class
-created many times
-data in

클래스만 정의하고 오브젝트만 만든다고 OOP 아니라
객체지향프로그래밍의 정말 중요한 원칙4을 따라야.

1.Encapsulation
관련있는 데이터와 함수를 한 오브젝트안에 -외부에서 볼수있고 없고 등을 넣으며 캡슐화
고양이의 내부 상태를 변경 <-외부 활동(펑션) 놀아주기, 밥주기 등으로

2.Abstraction
내부의 복잡한 기능을 다 이해하지 않고 외부에서 간단한 인터페이스를 통해 쓸 수 있는 것
커피 머신이 어떻게 돌아가는지 내부를 다 이해하지 않아도
기계에서 제공하는 간단한 버튼만 누르면 커피만들수 있다.

3.Inheritance
한번 잘 정의한 클래스를 재사용할 수 있다
(Parent-child)(super-sub)(base-derived)
IS-A 관계

makeSound()-animal -> dog, cat, pig… 동물을 상속해서 다 동물이다!

EventTarget -결국 모든 요소가 이벤트가 발생할 수 있구나
Node
Document, Element, Text
HTMLElement 클래스

4.Polymorphism
상속을 통해 어떤종류의 동물/커피머신을 만들던 공통된 함수로 접근할 수 있다. 다형성!