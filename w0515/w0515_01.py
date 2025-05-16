
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
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

# selenium 브라우저 동작
browser = webdriver.Chrome(options=options)

url = 'https://news.naver.com/main/ranking/popularDay.naver'
browser.get(url)


soup = BeautifulSoup(browser.page_source,'lxml')

f = open('w0515/news.csv','w',encoding='utf-8',newline='')
write = csv.writer(f)

title = ['언론사','기사제목']
write.writerow(title)       # csv에 리스트를 저장 

# 전체 기사 박스
data = soup.find('div',{'class':'rankingnews_box_wrap _popularRanking'})

# 언론사 별 박스
r_news = data.find_all('div',{'class':'rankingnews_box'})

# 언론사 이름
# journal = r_news[0].find('strong',{'class':'rankingnews_name'}).get_text().strip()
# headline = r_news[0].find('a',{'class':'list_title'}).get_text().strip()

for r in r_news:
    journal = r.find('strong',{'class':'rankingnews_name'}).get_text().strip()
    headline1 = r.find_all('a',{'class':'list_title'})[0].get_text().strip()
    headline2 = r.find_all('a',{'class':'list_title'})[1].get_text().strip()
    write.writerow([journal,headline1,headline2])
    

f.close()    

input('s')



# MIME 객체화
msg = MIMEMultipart('alternative')

# 정보
send_email = 'x_xitt@naver.com'
recvMails = 'x_xitt@naver.com'
password = 'N77MXDMPGXSC'
smtpName = "smtp.naver.com"
smtpPort = 587

# 메일 내용
html = MIMEText("""<h2>랭킹뉴스 기사모음</h2>
<img src='https://mail.naver.com/read/image/original/?mimeSN=1747271404.399860.348.14080&offset=1742&size=4808542&u=x_xitt&cid=c0debfdfc13115852259a7e225386ead@cweb014.nm&contentType=image/jpeg&filename=1747271399722.jpeg&org=1'>
""",
'html')
msg.attach(html)
msg['From'] = send_email
msg['Subject'] = '네이버 뉴스랭킹 보냄'

# 파일 객체 활성화?
part = MIMEBase('application','octet-stream')

# 파일 읽어오기
with open('w0515/news.csv','rb') as f:
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

s.sendmail(send_email,recvMails,msg.as_string())
s.close()

print('메일이 발송되었습니다.')