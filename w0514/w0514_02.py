import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
import random

# 크롬 옵션 설정 - 접근보안 해제
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")   # 자동화 티 안 나게??
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# 브라우저 실행
browser = webdriver.Chrome(options=options)
browser.maximize_window()   # 창 최대화
time.sleep(2)

# 야놀자
url = 'https://nol.yanolja.com/'
browser.get(url)

# 페이지 내 요소 찾기, 클릭
time.sleep(1)
browser.find_element(By.XPATH,'/html/body/div[10]/div/div/div/section/div[2]/button[2]').click()    # 광고창 닫기
time.sleep(1)
browser.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[2]/div/div[1]/a[11]/div/span[1]/img').click()   # 호텔/리조트 클릭
time.sleep(1)
browser.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[1]/div/div/button').click()     # 지역 선택
time.sleep(1)
browser.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div/div/div[1]/button[3]').click()     # 제주
time.sleep(1)
browser.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div/div/div[2]/div[1]/a[2]').click()  # 서귀포시/모들포
time.sleep(2)
browser.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/header/div[2]/div/button[1]').click()    # 날짜 선택
time.sleep(1)
browser.find_element(By.XPATH,'//*[@id="day-picker-2025-06"]/div[2]/div[1]/div[6]/button').click()    # 6월 6일
time.sleep(1)
browser.find_element(By.XPATH,'//*[@id="day-picker-2025-06"]/div[2]/div[1]/div[7]/button').click()    # 6월 7일
time.sleep(1)
browser.find_element(By.XPATH,'//*[@id="pc-dialog-sheet"]/div/div/div[3]/button').click()    # 적용하기
time.sleep(2)

# 현재높이 가져오기
prev_height = browser.execute_script("return document.body.scrollHeight;")

while True:     # 브라우저 높이가 더 늘어나지 않을 때까지
    # 스크롤 내리기 - 0에서부터 현재 높이까지 스크롤 내리기
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(1)
    # 변경된 현재높이 가져오기
    curr_height = browser.execute_script("return document.body.scrollHeight;")
    if prev_height == curr_height: break
    prev_height = curr_height


# html 파싱
soup = BeautifulSoup(browser.page_source,'lxml')
# with open('webdata/w0514/ya1.html','r',encoding='utf-8') as ff:
#     soup = BeautifulSoup(ff,'lxml')

# data = soup.find('div',{'class':'mb-[calc(76px+env(safe-area-inset-bottom))] flex h-full flex-col items-center overflow-x-hidden pc:mb-96'})
# a_list = data.find_all('a')
# print(len(a_list))

# for a in a_list:
#     title = a.find('p',{'class':'mb-4'}).get_text().strip()
#     rate = a.find('span',{'class':'typography-body-14-bold'}).get_text().strip()
#     reviews = a.find('span',{'class':'typography-body-14-bold'}).find_next_sibling().get_text().strip()[1:-1]
#     cost = a.find('span',{'class':'shrink-0 grow-0 text-text-neutral-main typography-subtitle-18-bold'})
    # if cost != None and len(title)<=8 :
    #     print(f'{title}\t\t{rate}\t{reviews}\t{cost.get_text().strip()}')
    # elif cost == None and len(title)<=8 :
    #     print(f'{title}\t\t{rate}\t{reviews}\t{cost}')
    # elif cost != None and len(title)>8 :
    #     print(f'{title}\t{rate}\t{reviews}\t{cost.get_text().strip()}')
    # else:
    #     print(f'{title}\t{rate}\t{reviews}\t{cost}')



# 파일 저장
with open("webdata/w0514/ya1.html",'w',encoding='utf-8') as f:
    f.write(soup.prettify())


input('dd...')