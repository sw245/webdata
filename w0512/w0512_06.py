import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import csv
import time



# url = 

# browser = webdriver.Chrome()
# browser.get('https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user')

# time.sleep(2)

# soup = BeautifulSoup(browser.page_source,'lxml')

# with open('webdata/w0512/coupang2.html') as f:
#     f.write(soup.prettify())


options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
    
    
# options = webdriver.ChromeOptions()

# options = webdriver.ChromeOptions()
# options = headless = True
# options.add_argument("window-szie=1920x1080")
# options.add_argument(Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7)
# options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7")

# 브라우저 실행
browser = webdriver.Chrome(options=options)

#페이지 접속
url = 'https://www.melon.com/chart/index.htm'
browser.get(url)

time.sleep(3)

soup = BeautifulSoup(browser.page_source,'lxml')

song1 = soup.tbody.find('tr',{'data-song-no':'38626852'})
tds_song1 = song1.find_all('td')
# print(len(tds_song1))
# for td in tds_song1:
#     print(td.get_text().strip())
    
print(tds_song1[1].find('span',{'class':'rank'}).get_text())
print(tds_song1[3].a['title'])
print(tds_song1[3].img['src'])
img_url = tds_song1[3].img['src']
img_res = requests.get(img_url)
with open('melon_chart1_jacket.jpg','wb') as f:
    f.write(img_res.content)
print(tds_song1[-6].a.get_text())

print(int(tds_song1[-5].find('span',{'class':'cnt'}).get_text()[-6:].replace(',','')))



input("아무 키나 눌러 종료")


# browser.maximize_window()

