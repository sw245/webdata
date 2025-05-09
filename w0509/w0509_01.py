
## 라이브러리
# requests:         html을 문자열로 가져옴
# beautifulsoup4:   html/xml에서 데이터 파싱을 쉽게 
# lxml:             css문법으로 특정 요소 가져옴

## selenium??

import requests

# 사이트 접속, html 소스를 가져옴
# res = requests.get('https://www.google.com/') # 접근 가능
# res = requests.get('https://www.melon.com/')  # 접근 불가
res = requests.get('https://www.naver.com/')    # 접근 불가

# 웹 접근제한 사이트 많아짐
if res.status_code == 200:
    print("정상 진행")
    print(res)
    print("응답코드 : ",res.status_code)    
    # 응답코드 200 - 정상코드, 400~404 - 페이지 없음/접근제한, 500 - 프로그램(서버) 에러
    print(res.text)     # 문자열로 출력
else:
    print("종료?")
    res.raise_for_status()      # 에러 시 종료 ?


