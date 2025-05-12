import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import csv
import time


options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
    


# 브라우저 실행
browser = webdriver.Chrome(options=options)

#페이지 접속
url = 'https://www.melon.com/chart/index.htm'
browser.get(url)

# time.sleep(3)

soup = BeautifulSoup(browser.page_source,'lxml')


## 1-100등 
# 순위, 곡정보,         가수, 좋아요, 이미지 링크 출력
# 1    너에게 닿기를    10cm, 59060, ~~~~
# 합계: 좋아요 총 개수 - ?

# 파일 저장 melon1.jpg - melon100.jpg

ranktitle = ['순위','곡정보','가수','좋아요','이미지 링크']

ff = open('webdata/w0512/melon_chart250512.csv','w',encoding='utf-8-sig',newline='')
writer = csv.writer(ff)
writer.writerow(ranktitle)

trs = soup.tbody.find_all('tr')
# print(len(trs))
likes_sum = 0
print('{}\t{}\t\t\t\t\t{}\t{}\t{}'.format(*ranktitle))
for i,tr in enumerate(trs):
    save = []
    tds = tr.find_all('td')
    rank = tds[1].find('span',{'class':'rank'}).get_text()
    title = tds[5].find_all('a')[0].get_text()
    artist = tds[5].find_all('a')[1].get_text()
    likes = tds[-5].find('span',{'class':'cnt'}).get_text()[4:].strip()
    img_url = tds[3].img['src']
    
    save = [rank,title,artist,likes,img_url]
    writer.writerow(save)
    print(f'{rank}\t{title}\t\t\t\t{artist}\t{likes}\n{img_url}')
    
    likes_sum += int(likes.replace(',',''))
    
    # img_res = requests.get(img_url)
    # with open(f'webdata/melon_jacket/melon{i+1}.jpg','wb') as f:
    #     f.write(img_res.content)
    
    
    
    
print('좋아요 합계 :',likes_sum)