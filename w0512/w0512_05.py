import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
import time



# url = 

browser = webdriver.Chrome()
browser.get('https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user')

time.sleep(2)

soup = BeautifulSoup(browser.page_source,'lxml')

with open('webdata/w0512/coupang2.html') as f:
    f.write(soup.prettify())
    
    
options = webdriver.ChromeOptions()



options = webdriver.ChromeOptions()
# options = headless = 