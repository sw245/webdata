import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
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

# 네이버 자동 로그인 메일 쓰기
url = 'https://www.naver.com'
browser.get(url)
time.sleep(2)

# 로그인 페이지 이동
elem = browser.find_element(By.CLASS_NAME,'MyView-module__naver_logo____Y442')
elem.click()

# 자바스크립트 사용 - 아이디, 비밀번호 입력

input_js = 'document.getElementById("id").value = "";\
            document.getElementById("pw").value = "";'
time.sleep(random.uniform(2,4))
browser.execute_script(input_js)    # 자바스크립트 코드 실행
time.sleep(random.uniform(2,4))

# 로그인 버튼 누르기
elem = browser.find_element(By.CLASS_NAME,'btn_login')
elem.click()



# # 아이디 입력
# elem = browser.find_element(By.ID,"id")
# elem.send_keys('dkgk1002p')
# time.sleep(random.uniform(2,4))

# # 비밀번호 입력
# elem = browser.find_element(By.ID,"pw")
# elem.send_keys("1111")
# time.sleep(random.uniform(2,4))


input('dd')