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
url = 'https://www.gmarket.co.kr/n/best'
browser.get(url)

# time.sleep(3)
# input("asd")

soup = BeautifulSoup(browser.page_source,'lxml')

print(soup.find('div',{'class':'box__best-list'}).find('li',{'class':'list-item'}).p.get_text())