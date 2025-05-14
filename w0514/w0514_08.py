
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


# 퀴즈
# 신문사, 기사 제목 >> news.csv파일 저장
# 파일첨부 메일로 발생
# 제목: 네이버 뉴스랭킹 보냄
# 내용: 네이버 12개 랭킹 1위 뉴스를 보냅니다.
# 수신인 : onulee@naver.com


# # csv 파일로 저장

# ff = open('webdata/w0514/news.csv','w',encoding='utf-8',newline='')
# writer = csv.writer(ff)

# writer.writerow(['언론사','뉴스 헤드라인'])

# # selenium 브라우저 동작
# browser = webdriver.Chrome(options=options)

# url = 'https://news.naver.com/main/ranking/popularDay.naver'
# browser.get(url)
# time.sleep(2)



# # 뉴스 긁어오기

# for i in range(12):
#     browser.find_element(By.XPATH,f'//*[@id="wrap"]/div[4]/div[2]/div/div[{i+1}]/ul/li[1]/div/a').click()
#     time.sleep(2)
    
#     soup = BeautifulSoup(browser.page_source,'lxml')
#     journal = soup.find('span',{'class':'media_end_head_top_logo_text light_type _LAZY_LOADING_ERROR_SHOW'}).get_text()
#     title = soup.find('h2',{'id':'title_area'}).span.get_text()
#     writer.writerow([journal,title])
    
#     browser.back()
#     time.sleep(2)


# ff.close()

# input('ok')


# MIME 객체화
msg = MIMEMultipart('alternative')

# 정보
send_email = ''
recvMails = ['','']
password = ''
smtpName = "smtp.naver.com"
smtpPort = 587

# 메일 내용
text = MIMEText('네이버 12개 랭킹 1위 뉴스를 보냅니다.')
msg.attach(text)
msg['From'] = send_email
msg['Subject'] = '네이버 뉴스랭킹 보냄'

# 파일 객체 활성화?
part = MIMEBase('application','octet-stream')

# 파일 읽어오기
with open('webdata/w0514/news.csv','rb') as f:
    # part에 담기
    part.set_payload(f.read())
    
# 파일 첨부할 수 있는 형태로 인코딩
encoders.encode_base64(part)

# header 정보
part.add_header('Content-Disposition','attachment',filename='news.csv')
# 파일 첨부
msg.attach(part)

# 메일 발송
s = smtplib.SMTP(smtpName,smtpPort)
s.starttls()
s.login(send_email,password)

for m in recvMails:
    msg['To'] = m
    s.sendmail(send_email,m,msg.as_string())
s.close()

print('메일이 발송되었습니다.')