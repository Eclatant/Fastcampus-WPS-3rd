# 추가사항

### Token Authentication 사용시 EB 세팅

> 근택님이 제보해주셨습니다  
> 매우감사합니당  
> 밥 사드리겠습니당(굽신)

config파일에 아래 내용을 적어줍니다.  
Apache에서는 기본적으로 Session인증만을 지원하기 때문에, 아래 문구를 사용해서 세션 이외의 인증을 허용해야 합니다.

```
container_commands:
  01_wsgipass:
    command: 'echo "WSGIPassAuthorization On" >> ../wsgi.conf'
```


