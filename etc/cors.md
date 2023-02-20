Access-Control-Allow-Origin 헤더가 없다는 에러
-> 브라우저와 서버의 도메인이 일치하지 않으면 요청이 차단.
(서버->서버는 ok)

Cross Origin Resource Sharing

=>
서버의 응답 헤더 + Access-Control-Allow-Origin
cors 패키지 설치 후 적용
ex:
```
const cors = require('cors');
//이제 헤더 추가됌
router.use(cors({
   // 다른 도메인 간의 쿠키가 공유(서버 간 도메인이 달라도 로그인 ok)
   credentials: true,
}))
```
* 새로운 문제: 요청보내는 주체가 클라이언트라서, 비밀키(process.env.CLIENT._SECRET)이 모두에게 노출

1)허용 호스트와 비밀 키가 모두 일치할 때만 CORS 허용케 수정

```
const cors = require('cors');
const url = require('url');
const {Domain} = require('../models);

router.use(async(req, res, next) => {
   const domain = await Domain.findOne({
      where: { host: url.parse(req.get('origin')).host },
   });
   if (domain) {
      cors({
         origin: req.get('origin'),
         credentials: true,
      })(req, res, next);
   } else {
      next();
   }
});
```


2) 또는 프록시(대리인) 서버 사용
- 서버간 요청시에는 CORS 문제가 발생하지 않는다는 것에서...
직접 서버구현 또는 npm i httmp-proxy-middleware 패키기 사용