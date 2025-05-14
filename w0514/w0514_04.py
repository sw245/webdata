## selenium

# 1. 네이버 접속
# 2. 뉴스 클릭 > 새 창으로 열림
# 3. 뉴스 랭킹 > 각 1위, 12개의 뉴스를 출력

# 일단: 상단 첫 번째 뉴스 출력

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")   # 자동화 티 안 나게??
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

browser = webdriver.Chrome(options=options)

url = 'https://www.naver.com'
browser.get(url)
time.sleep(1)

# news_xpath = ['//*[@id="wrap"]/div[4]/div[2]/div/div[1]/ul/li[1]/div/a',    # 왼쪽 첫번 째 기사
#               '//*[@id="wrap"]/div[4]/div[2]/div/div[2]/ul/li[1]/div/a']       


browser.find_element(By.XPATH,'//*[@id="shortcutArea"]/ul/li[5]/a').click()     # 뉴스 클릭
browser.switch_to.window(browser.window_handles[1])
time.sleep(1)
    
browser.find_element(By.XPATH,'/html/body/section/header/div[2]/div/div/div/div/div/ul/li[8]/a').click()    # 랭킹 탭 클릭
time.sleep(1)



title_list = []

for i in range(12):
    browser.find_element(By.XPATH,f'//*[@id="wrap"]/div[4]/div[2]/div/div[{i+1}]/ul/li[1]/div/a').click()
    time.sleep(1)
    soup = BeautifulSoup(browser.page_source,'lxml')
    title = soup.find('h2',{'id':'title_area'}).span.get_text()
    title_list.append(title)
    browser.back()
    time.sleep(1)

for t in title_list:
    print(t)

news_selec = input("뉴스 내용 확인: 번호 입력 >")
browser.find_element(By.XPATH,f'//*[@id="wrap"]/div[4]/div[2]/div/div[{news_selec}]/ul/li[1]/div/a')
soup = BeautifulSoup(browser)


# browser.find_element(By.XPATH,)


input('stop')


