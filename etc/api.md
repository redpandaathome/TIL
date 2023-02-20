# RESTful API

참고: https://youtu.be/iOueE9AXDQQ

`api`
소프트웨어가 소프트웨어로부터
지정된 형식으로 요청, 명령을 받을 수 있는 수단
Application programming interface 
네트워크밖에서도… ex)window api (버튼클릭->동작수행)

과거 soap ->rest
rest가장 큰특징: 요청이 어떤 동작이나 정보를 위한것인지 추론가능

혼자만드는게 아니니…협업을위해!
주소만 봐도 요청파악이 가능해야하는데

Class/2/students
URI:자원을 구조와 함께 나타내는 구분자 
* URI(identifier) > URL(location), URN(name)
서버에 rest api로 요청을 보낼 땐 http 규약에 따라 신호전송
HTTP로 요청 보낼시 여러 메소드가 있다
REST API에서는 이 중 4-5가지 사용(get, post, delete, put, patch)

(Post, put, patch) - body 정보를 비교적 많이 안전하게 감춰 실어보낼 수 있다.

누구든 각 요청의 의도를 쉽게 파악할 수 있도록하기 위해서 목적에 따라 구분해서 사용

```Get : ~/classes/2/students
Post: ~/classes/2/students
Put | patch: ~/14 (14번학생수정)
put은 정보를 통째로 갈아 끼울 때
patch는 일부를 특정방식으로 변경
Delete: ~/14 (14번 학생 그만둠)
```

uri에 동작까지 표시할 필요가 없어진다 =>uri는 동사가아닌 명사로 이뤄져야 한다.
```
Ex: 기존
/classes/2/students/create
/classes/2/students/read
/classes/2/students/3/update
/classes/2/students/3/delete
```

즉 REST API란, 
HTTP 요청을 보낼 때
어떤 URI에 어떤 메소드를 사용할지 (+기타)
개발자들 사이에 널리 지켜지는 약속
-형식이기에 기술에 구애받지 않음
앱/웹/파이썬/노드 상관없이 소프트웨어간 http로 정보를 주고받는 부분이 있다면, 이 형식/규칙들을 준수해서 RESTful한 서비스를 만들자