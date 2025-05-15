## requests
# find, find_all


## selenium
# find_element(By.XPATH)


## BeautifulSoup
# soup = BeautifulSoup(res.text,'lxml')
# soup = BeautifulSoup(browser.page_source,'lxml')



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
from pyautogui import *    # 마우스 제어

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders



options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")   # 자동화 티 안 나게??
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# selenium 브라우저 동작
browser = webdriver.Chrome(options=options)

url = 'https://new.land.naver.com/complexes/102737?ms=37.5373434,127.0100999,17&a=APT:PRE:ABYG:JGC&e=RETAIL'
browser.get(url)

moveTo(50,700)
sleep(1)


pre_height = int(browser.execute_script("return articleListArea.scrollHeight"))
print("처음 화면 높이 :",pre_height)
# 자바스크립트 스크롤 내리기
# browser.execute_script(f"window.scroll(0,{pre_height})")
moveTo(50,700)
# scroll(-pre_height) # 마우스 휠로 스크롤 내리기
sleep(2)

while True:
    scroll(-pre_height)
    sleep(1)
    curr_height = browser.execute_script("return articleListArea.scrollHeight")
    print("변화된 현재 높이 :",curr_height)
    if curr_height == pre_height: break
    pre_height = curr_height

soup = BeautifulSoup(browser.page_source,'lxml')

box = soup.find_all('div',{'class':'item_inner'})

print(len(box))
print('아파트\t\t가격\t\t스펙')

for b in box:
    apt = b.find('span',{'class':'text'}).get_text()
    aptype = b.find('span',{'class':'type'}).get_text()
    aprice = b.find('span',{'class':'price'}).get_text()
    # if aptype != '월세' :
    #     aprice_p = aprice[:3]
    #     if aprice_p.isdigit():
    #         aprice_p = int(aprice_p)
    #     else: aprice_p = int(aprice_p[:-1])
    # else:
    #     aprice_p = int(aprice.split('/')[0][:-1])
    aprice_p = int(aprice.split('억')[0])   # 위 if문을 대체 가능
    apec = b.find('span',{'class':'spec'}).get_text()
    if aptype == '전세' and aprice_p <= 30:
        print(f'{apt}\t{aptype} {aprice}\t{apec}')
    
    





input('코드 실행 종료')