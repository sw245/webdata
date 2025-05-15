
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
import pyautogui    # 마우스 제어

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

url = 'https://www.daum.net'
browser.get(url)

# pyautogui 마우스 제어 라이브러리
# 자바스크립트 명령어 스크롤이 내려가지 않을 경우 마우스 휠로 스크롤하기 위해 사용

pyautogui.sleep(1)
# pyautogui.click()
# pyautogui.doubleClick()
pyautogui.scroll(-1200)      # 아래방향으로 이동
pyautogui.scroll(500)
pyautogui.sleep(2)
pyautogui.moveTo(800,500)
pyautogui.sleep(1)
pyautogui.moveTo(500,500)
pyautogui.click()

input("ㅁㄴㅇㄴㅁㅇ")