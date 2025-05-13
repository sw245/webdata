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

# 네이버 자동 로그인 메일 쓰기
url = 'https://www.naver.com'
browser.get(url)
time.sleep(2)

# # 클릭 이벤트
# elem = browser.find_element(By.CLASS_NAME,"MyView-module__naver_logo____Y442")
# elem.click()

# 글자입력 이벤트
elem = browser.find_element(By.ID,'query')
elem.send_keys('네이버 로그인')
time.sleep(2)

# 엔터 키 입력
elem.send_keys(Keys.ENTER)

# 클릭
elem = browser.find_element(By.CLASS_NAME,'logo_slogan')
elem.click()

time.sleep(2)

# 크롬브라우저 탭을 처음으로 이동 (현재 탭 옮기기?)
browser.switch_to.window(browser.window_handles[0])

# 뒤로 가기
browser.back()
time.sleep(2)

# 앞으로 가기
browser.forward()
time.sleep(2)



input("...")




# print(browser.page_source)
# soup = BeautifulSoup(browser.page_source,'lxml')