


# 네이버 검색 '날씨'
# 기온, '구름많음', 미세먼지 '보통' 출력



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

# url = 'https://www.naver.com'
# browser.get(url)

# elem = browser.find_element(By.ID,'query')
# time.sleep(1)
# elem.send_keys('날씨')
# elem.send_keys(Keys.ENTER)
# time.sleep(2)

# soup = BeautifulSoup(browser.page_source,'lxml')

# temper = soup.find('div',{'class':'temperature_text'}).strong.get_text()[5:]
# weather = soup.find('span',{'class':'weather before_slash'}).get_text()

# print(temper)
# print(weather)


url2 = 'https://weather.naver.com'
browser.get(url2)

soup = BeautifulSoup(browser.page_source,'lxml')
timesleep

print(soup)

# data = soup.find('ul',{'class':'box_color'})
# print(data)

# lis = data.find_all('li')
# for li in lis:
#     print(li.get_text())



input('ㄴㄴ')