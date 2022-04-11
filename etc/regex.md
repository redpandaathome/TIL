https://github.com/dream-ellie/regex
https://regexr.com/5mhou
https://regexone.com/

q1. phone number
\d{2,3}[- .]\d{3}[- .]\d{4}

q2. email
[a-zA-Z0-9._+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-0.]+

q3. youtube id
(?:https?:\/\/)?(?:w{3}\.)?(?:youtu.be\/)([-a-zA-Z0-9]+)

```
const regex = /(?:https?:\/\/)?(?:w{3}\.)?(?:youtu.be\/)([-a-zA-Z0-9]+)/;
const url = 'http://www.youtu.be/-ZClicWm0zM';
let result= url.match(regex);
result[1]
```