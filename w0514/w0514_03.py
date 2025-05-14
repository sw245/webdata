import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
import random

# web scraping - BeautifulSoup으로
with open('webdata/w0514/ya1.html','r',encoding='utf-8') as f:
    soup = BeautifulSoup(f,'lxml')

# 검색된 리스트 전체    
data = soup.find('div',{'class':'mb-[calc(76px+env(safe-area-inset-bottom))] flex h-full flex-col items-center overflow-x-hidden pc:mb-96'})

# 검색된 호텔 정보
a_list = data.find_all('a')
# print(len(a_list))

# 호텔 이름
title = a_list[0].find('p',{'class':'mb-4 line-clamp-2 text-start text-fill-neutral-main typography-subtitle-16-bold'}).get_text().strip()
# print(title)

# 평점
rate = a_list[99].find('span',{'class':'typography-body-14-bold'}).get_text().strip()
if rate != '후기': rate = float(rate)       # rate.isdigit() 으로도 확인 가능
# print(rate)    

# 평가 수
rate_num = a_list[0].find('span',{'class':'typography-body-14-bold'}).find_next_sibling().get_text().strip()[1:-1]
print(rate_num)

# 비용
cost = a_list[0].find('span',{'class':'shrink-0 grow-0 text-text-neutral-main typography-subtitle-18-bold'}).get_text().strip()
print(cost)

sorting = []

for a in a_list:
    title = a.find('p',{'class':'mb-4 line-clamp-2 text-start text-fill-neutral-main typography-subtitle-16-bold'}).get_text().strip()
    rate = a.find('span',{'class':'typography-body-14-bold'}).get_text().strip()
    if rate != '후기': rate = float(rate)
    rate_num = a.find('span',{'class':'typography-body-14-bold'}).find_next_sibling().get_text().strip()[1:-1]
    cost = a.find('span',{'class':'shrink-0 grow-0 text-text-neutral-main typography-subtitle-18-bold'})
    if cost == None: cost = '예약 마감'
    else:   cost = cost.get_text().strip()
    # print(f'{title}\t{rate}\t{rate_num}\t{cost}')
    
    # 평점이 4.1보다 낮거나 평가 수가 500 미만인 것은 제외
    if rate == '후기' or rate < 4.1 or int(rate_num.replace(',','')) < 500: continue
    print(f'{title}\t{rate}\t{rate_num}\t{cost}')
    
    # 위 필터를 평점 순으로 정렬
    sorting.append([title,rate,rate_num,cost])
    