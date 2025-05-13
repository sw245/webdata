
# import requests
# from bs4 import BeautifulSoup
# import csv
# import time

# url = 'https://www.gmarket.co.kr/n/best'
# # 옵션 설정
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'}
# res = requests.get(url,headers=headers)
# res.raise_for_status()
# 403 에러 발생

# print(res.text)     # 소스 출력

# soup = BeautifulSoup(res.text,'lxml')

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import csv
import time

# 크롬 옵션 설정 
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
# 셀레니움 접근 제한 >> 보안접근 해제

# 브라우저 실행
browser = webdriver.Chrome(options=options)

# 페이지 접속
# url = 'https://co1140.shiningcorp.com/index.php?device=pc&designkits=1'
url = 'https://www.gmarket.co.kr/n/best'
browser.get(url)
time.sleep(2)



# print(browser.page_source)

soup = BeautifulSoup(browser.page_source,'lxml')

# data = soup.find('div',{'class':'list-best'})
data = soup.find('div',{'id':'container'})
ul = data.find('ul',{'class':'list__best'})
lis = ul.find_all('li')

sum_price = 0
for i,li in enumerate(lis):
    if i == 10: break
    txt = li.get_text()
    print(txt[:txt.find('쿠폰')],end='\t')  # 제목에 '쿠폰'이 들어가버린 항목이 있음....
    print(txt[txt.find('판매가')+3:])
    
    price = int(txt[txt.find('판매가')+3:-1].replace(',',''))
    sum_price += price
    
print(sum_price)



# 1-10위 제목,가격 출력
# 총합계 가격 출력

# print(lis)


# 파일 저장 후 저장된 파일으로 스크래이핑해도 됨.

# with open('temple1.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())
    
    
# 프로그램 종료
# input("프로그램 종료 >")