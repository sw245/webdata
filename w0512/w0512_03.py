import requests
from bs4 import BeautifulSoup   # parsing
import csv

url = 'https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user'
headers = {
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
   "Accept-Language": "ko-KR,ko;q=0.9",
   "Referer": "https://www.coupang.com/",
}
res = requests.get(url,headers=headers)

res.raise_for_status()  # 에러 대비

soup = BeautifulSoup(res.text,'lxml')

# print(soup)
# >> 자바스크립트로 페이지 구현됨.


with open('webdata/w0512/coupang.html','w',encoding='utf-8') as f:
    f.write(soup.prettify())
    # soup = BeautifulSoup(f,'lxml')
    
    
    