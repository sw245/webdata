# #  1. 네이버 접속 2. 검색어 '시가총액' 3. 엔터 키 4. 삼성전자

# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# import csv
# import time
# import random


# # 크롬 옵션 설정 
# options = Options()
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument("start-maximized")
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# # 셀레니움 접근 제한 >> 보안접근 해제


# browser = webdriver.Chrome(options=options)

# url = 'https://www.naver.com'
# browser.get(url)

# elem = browser.find_element(By.XPATH,'//*[@id="query"]')
# elem.send_keys('시가 총액')
# elem.send_keys(Keys.ENTER)

# elem = browser.find_element(By.XPATH,'//*[@id="main_pack"]/section[1]/div/div[2]/div[2]/div[1]/div[1]/table/tbody/tr[1]/th/a')
# elem.click()





### 저장된 페이지에서 데이터 가져오기

from bs4 import BeautifulSoup


### fly1.html 불러오기
## 항공사, 출발시간, 도착시간, 금액

ff = open('w0513/flights.html','r',encoding='utf-8')

soup = BeautifulSoup(ff,'lxml')

# print(soup)

divs = soup.find_all('div',{'class':'domestic_Flight__8bR_b'})
# print(len(divs))
cost_list = []
flight_info = []
flights = []
for div in divs:
    airline = div.find('b',{'class':'airline_name__0Tw5w'}).get_text().strip()
    departure = div.find('b',{'class':'route_time__xWu7a'}).get_text().strip()
    arrival = div.find_all('b',{'class':'route_time__xWu7a'})[1].get_text().strip()
    cost = div.find('i',{'class':'domestic_num__ShOub'}).get_text().strip()
    if int(cost.replace(',','')) not in cost_list : ## 중복 없애기
        cost_list.append(int(cost.replace(',','')))
    flight_info = [airline, departure, arrival, cost.replace(',','')]
    flights.append(flight_info)
    # if airline == '진에어':
    #     print(f'{airline}\t\t{arrival}\t{departure}\t{cost}')    
    # else:
    #     print(f'{airline}\t{arrival}\t{departure}\t{cost}')
        
# print(cost_list)

cost_rank = int(input(f"가격이 낮은 순으로 몇 번째의 항공편을 조회하시겠습니까? (총 항공편 수 : {len(cost_list)}) >"))

# print(sorted(cost_list))

for f in flights:
    if str(sorted(cost_list)[cost_rank-1]) in f:
        print(f)
        


# ## 최저가/최고가 list 정렬
# sorted(flights,key=lambda x:x[3])   # flights의 요소 중 [3]번째 항목으로 정렬 (숫자로 정렬하려면 int타입이어야 함)
# sorted(flights,key=lambda x:x[3],reverse=True) # 역순 정렬



        
# print(sorted(cost_list))
# print(sorted(cost_list,reverse=True))
        
ff.close()





# ### selenium으로 데이터 가져오기

# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# options = Options()
# options.add_argument("--disable-blink-features=AutomationControlled")   # 자동화 티 안 나게
# options.add_argument("start-maximized")
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
# options.add_experimental_option("excludeSwitches",["enable-automation"])
# options.add_experimental_option("useAutomationExtension",False)

# browser = webdriver.Chrome(options=options)

# url = 'https://flight.naver.com/'
# browser.get(url)
# time.sleep(2)

# elem = 

