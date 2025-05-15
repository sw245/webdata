### 네이버 항공권

# 김포, 제주 5/31~6/4
# 금액 110,000원 이하 제외
# 출발시간 5/31 17:00 이후 제외

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import smtplib
import pyautogui


options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")   # 자동화 티 안 나게??
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)


browser = webdriver.Chrome(options=options)

url = 'https://flight.naver.com/'
browser.get(url)
time.sleep(2)

# input('aa')

xpath_click = ['//*[@id="layer"]/button[1]',      # '7일간 보지 않기'
               '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[1]/b',   # 출발 클릭
               '//*[@id="__next"]/div/main/div[8]/div[2]/div/div/ul[1]/li[3]/button',   # 김포 클릭
               '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[2]/b',   # 도착 클릭
               '//*[@id="__next"]/div/main/div[8]/div[2]/div[2]/div[2]/ul[1]/li[1]/button',  # 제주 클릭
               '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[1]',     # 가는 날 클릭
               '//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div/div[2]/table/tbody/tr[5]/td[7]/button',  # 5/31 클릭
               '//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div/div[3]/table/tbody/tr[1]/td[4]/button',  # 6/4 클릭
               '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button',   # 항공권 검색 클릭
               ]

for i in range(len(xpath_click)):
    browser.find_element(By.XPATH,xpath_click[i]).click()
    time.sleep(1)

prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script(f"window.scrollTo(0,{prev_height})")
    time.sleep(1)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height: break
    prev_height = curr_height
    

soup = BeautifulSoup(browser.page_source,'lxml')

flights = soup.find_all('div',{'class':'domestic_Flight__8bR_b'})

count = 0

for f in flights:
    airline = f.find('b',{'class':'airline_name__0Tw5w'}).get_text()
    departure = f.find_all('span',{'class':'route_airport__tBD9o'})[0].find('b',{'class':'route_time__xWu7a'}).get_text()
    arrival = f.find_all('span',{'class':'route_airport__tBD9o'})[1].find('b',{'class':'route_time__xWu7a'}).get_text()
    cost = f.find('i',{'class':'domestic_num__ShOub'}).get_text()
    cost_p = int(cost.replace(',',''))
    departure_p = int(departure.replace(':',''))
    
    if cost_p <= 110000 or departure_p >= 1700: continue
    if len(airline) < 4:
        print(f'{airline}\t\t{departure}\t{arrival}\t{cost}')
        count += 1
    else:
        print(f'{airline}\t{departure}\t{arrival}\t{cost}')
        count += 1
    
print(len(flights))
print(count)



input('dd')