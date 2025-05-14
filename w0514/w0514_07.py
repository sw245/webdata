import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

## MIME 객체화
msg = MIMEMultipart('alternative')

#
send_email = ''
recv_email = ''
password = ''
smtpName = "smtp.naver.com"
smtpPort = 587

## 내용부분
text = "안녕"
part2 = MIMEText(text)
msg.attach(part2)
msg['From'] = send_email
msg['To'] = recv_email
msg['Subject'] = '2025년 5월 14일 수요일'

## 파일첨부
part = MIMEBase('application','octet-stream')

## 파일 읽어오기
with open('webdata/w0512/melon_chart250512.csv','rb') as f:
    # part 담기
    part.set_payload(f.read())
    
# 파일을 첨부할 수 있는 형태로 인코딩
encoders.encode_base64(part)
## header 정보
part.add_header('Content-Disposition','attachment',filename='melon_chart250512.csv')
msg.attach(part)


# 메일 발송 부분
s = smtplib.SMTP(smtpName,smtpPort)
s.starttls()
s.login(send_email,password)

## 보내는 주소가 네이버메일이 아니면 에러 발생 ??
s.sendmail(send_email,send_email,msg.as_string())
s.close()


print("메일이 발송되었습니다.")