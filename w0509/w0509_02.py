import requests

# 쿠팡에 접근해서 rest.text 출력

# res = requests.get('https://www.coupang.com/')
# res = requests.get('https://www.daum.net/')
# url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent/'
# url = 'https://www.daum.net/'
# url = 'https://www.coupang.com/'
# url = 'https://www.melon.com/'
url = 'https://www.google.com/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'}
# 원래 user-agent: python-requests/2.32.3
res = requests.get(url,headers=headers)

res.raise_for_status()  # 에러 시 종료

print(res.text)
with open('w0509/test.html','w',encoding='utf-8') as f:
    f.write(res.text)
print("[ 프로그램 종료 ]")

# print(res)
# print(res.status_code)


