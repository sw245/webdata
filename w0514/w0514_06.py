import requests
import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup

## 텍스트만 보낼 수 있음

# smtpName = "smtp.naver.com"
# smtpPort = 587

# sendEmail = ""
# password = ""

# recv_email = ""


url = 'https://weather.naver.com/'
res = requests.get(url)
res.raise_for_status

soup = BeautifulSoup(res.text,'lxml')
print(soup)

soup.find('div',{'class':'card_current_date card_slide_item _cnTomorrow'})




# # 메일 내용
# text = "날씨정보: 오늘 날씨 - 구름 많음, 내일 날씨 - 흐리고 비"

# msg = MIMEText(text)
# msg['Subject'] = "웹이메일 보내기"
# msg['From'] = sendEmail
# msg['To'] = recv_email

# s = smtplib.SMTP(smtpName,smtpPort)
# s.starttls()
# s.login(sendEmail,password)
# s.sendmail(sendEmail,recv_email,msg.as_string())
# s.close()

# print("메일이 발송되었습니다.")