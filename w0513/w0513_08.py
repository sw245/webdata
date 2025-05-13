# import requests

# 1. 호텔/리조트 클릭, 
# 2. 지역선택 클릭, 제주 클릭, 서귀포/모슬포 클릭 
# 3. 날짜선택 클릭, 6/7~8 선택, 적용하기 클릭 ,
# 4. 스크롤 내리기 끝까지,
# 5. 업종(호텔)/호텔이름/평점(없으면 '없음' 출력)/후기 개수/비용    출력

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

browser = webdriver.Chrome(options=options)

url = 'https://nol.yanolja.com/'
browser.get(url)
time.sleep(3)

# input('왜 다른 페이지인데...')

click_xpath = ['/html/body/div[1]/div/div[3]/div/div[2]/div/div[1]/a[1]',      # 호텔/리조트
               '/html/body/div[1]/div/div[2]/div/div[1]/div/div[1]/button',     # 지역선택
               '//*[@id="_MODAL_DIM_"]/div/section/div[2]/div[1]/button[3]',    # 제주
               '//*[@id="_MODAL_DIM_"]/div/section/div[2]/div[2]/div/div/button[2]',    # 서귀포/모슬포
               '/html/body/div[1]/div/div[1]/div[1]/header/div[2]/div/button[1]',       # 날짜선택    
               '//*[@id="day-picker-2025-06"]/div[2]/div[1]/div[7]/button',     # 6/7
               '//*[@id="day-picker-2025-06"]/div[2]/div[2]/div[1]/button',     # 6/8
               '//*[@id="pc-dialog-sheet"]/div/div/div[3]/button'      # 적용하기
               ]       

for i in range(len(click_xpath)):
    elem = browser.find_element(By.XPATH,click_xpath[i])
    elem.click()
    time.sleep(2)
    
# 스크롤 내리기 (자바스크립트 활용)

prev_height = browser.execute_script("return document.body.scorllHeight;")      # 현재 창의 맨 밑 좌표 값 
while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")        # 0에서 맨 밑으로 scroll
    time.sleep(1)       # 페이지 로딩 기다리기 (페이지 높이가 늘어남)
    curr_height = browser.execute_script("return document.body.scrollHeight;")      # 현재 맨 밑 좌표값 업데이트
    if curr_height == prev_height: break        # 늘어난 높이와 이전 높이가 같으면 (늘어나지 않았으면) 반복문 끝
    prev_height = curr_height       # 이전 높이 업데이트 (다시 늘리기 전 현재 높이)
    


input('...')