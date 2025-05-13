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
browser.maximize_window()   # 창 최대화
time.sleep(2)

# 네이버 항공권
url = 'https://flight.naver.com'
browser.get(url)

click_xpath = ['//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[1]/b',
               '//*[@id="__next"]/div/main/div[8]/div[2]/div/div/ul[1]/li[3]/button',
               '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[2]',
               '//*[@id="__next"]/div/main/div[8]/div[2]/div[2]/div[2]/ul[1]/li[1]/button',
               '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[1]',
               '//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div/div[3]/table/tbody/tr[2]/td[5]/button',
               '//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div/div[3]/table/tbody/tr[2]/td[7]/button',
               '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button']


for i in range(len(click_xpath)):
    elem = browser.find_element(By.XPATH,click_xpath[i])
    elem.click()
    time.sleep(1)
    

# 검색버튼 클릭 후 화면이 나타날때까지 대기
# WebDriverWait(browser,10).until(EC.presence_of_all_elements_located(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div[2]/div[2]/div[1]'))
time.sleep(6)

# soup = BeautifulSoup(browser.page_source,'lxml')

# print(soup.find_all('i',{'class':'domestic_num__ShOub'}))
    
# elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div/div/ul[1]/li[3]/button')
# elem.click()

# elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[2]')
# elem.click()

### 스크롤 내리기
# 현재 사이트 높이를 가져오는 자바스크립트
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # 자바스크립트 실행 ## 브라우저 높이 0에서 현재 높이까지 스크롤 내리기
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    # 변동된 현재 문서 높이를 가져오기
    curr_height = browser.execute_script("return document.body.scrollHeight")
    # 스크롤 높이가 변동이 없을 시
    if curr_height == prev_height: break
    prev_height = curr_height   # 현재 높이를 다시 입력해서 스크롤 내리기 재실행
    
print("스크롤 내리기 종료")

## webscraping
soup = BeautifulSoup(browser.page_source,'lxml')
with open('w0513/flights.html','w',encoding='utf-8') as f:
    f.write(soup.prettify())
    
print("파일 저장 완료")




input('asdsd')

