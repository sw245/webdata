
## 임시 패스워드: aaa1111

## 자신에게 보내기
## onulee@naver.com

html = """
<html xmlns="http://www.w3.org/1999/xhtml" lang="ko" xml:lang="ko">
<head>
<meta http-equiv="Content-Type" content="application/xhtml+xml; charset=utf-8" />
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
<title> 비밀번호 발송 </title>


</head>
<body bgcolor="#FFFFFF" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" style="margin:0; padding:0; font:normal 12px/1.5 돋움;">


<table width="700" cellpadding="0" cellspacing="0" align="center">
<tr>
	<td style="width:700px;height:175px;padding:0;margin:0;vertical-align:top;font-size:0;line-height:0;">
		<img src="https://mail.naver.com/read/image/original/?mimeSN=1747272987.123781.166.30464&offset=1773&size=4808542&u=x_xitt&cid=5caf185a758f01dca33b1652c4c918@cweb016.nm&contentType=image/jpeg&filename=1747272950588.jpeg&org=1" />					
	</td>
</tr>
<tr>
	<td style="width:700px;height:78px;padding:0;margin:0;vertical-align:top;">
		<p style="width:620px;margin:50px 0 40px 38px;text-align:center;font-size:0;line-height:0;"><img src="https://mail.naver.com/read/image/original/?mimeSN=1747272987.123781.166.30464&offset=4810610&size=4805124&u=x_xitt&cid=7ed1c70caa1625351dfc2fac7b952c@cweb012.nm&contentType=image/jpeg&filename=1747272961333.jpeg&org=1" alt="원두커피의 名家, JARDIN 임시 비밀번호가 발급되었습니다." /></p>
	</td>
</tr>
<tr>
	<td style="width:700px;height:196px;padding:0;margin:0;vertical-align:top;">
		<table width="618" height="194" cellpadding="0" cellspacing="0" align="center" style="margin:0 0 0 40px;border:1px #d9d9d9 solid;">
		<tr>
			<td style="width:618px;height:194px;padding:0;margin:0;vertical-align:top;font-size:0;line-height:0;background:#f9f9f9;">
				<p style="width:620px;margin:30px 0 0 0;padding:0;text-align:center;"><img src="https://mail.naver.com/read/image/original/?mimeSN=1747273032.914716.170.34560&offset=9529431&size=4766834&u=x_xitt&cid=511ca48bce64e2a255eae2a58688e5a8@cweb017.nm&contentType=image/jpeg&filename=1747273029364.jpeg&org=1" alt="JARDIN에서 비밀번호 찾기를 요청하셨습니다." /></p>
				<p style="width:620px;margin:10px 0 0 0;padding:0;text-align:center;color:#888888;font-size:12px;line-height:1;">아래의 PASSWORD는 임시 PASSWORD이므로 홈페이지 로그인 후 다시 수정해 주십시오.</p>
				<p style="width:620px;margin:28px 0 0 0;padding:0;text-align:center;color:#666666;font-size:12px;line-height:1;"><strong>임시 패스워드 : <span style="color:#f7703c;line-height:1;">dasdw2341</span></strong></p>
				<p style="width:620px;margin:30px 0 0 0;padding:0;text-align:center;color:#888888;font-size:12px;line-height:1.4;">쟈뎅샵에서는 고객님께 보다 나은 서비스를 제공하기 위해 항상 노력하고 있습니다.<br/>앞으로 많은 관심 부탁드립니다.</p>
			</td>
		</tr>
		</table>	
	</td>
</tr>
<tr>
	<td style="width:700px;height:120px;padding:0;margin:0;vertical-align:top;">
		<p style="width:700px;margin:30px 0 50px 0;text-align:center;"><a href="#"><img src="https://mail.naver.com/read/image/original/?mimeSN=1747273032.914716.170.34560&offset=4759358&size=4769776&u=x_xitt&cid=4e62d6c946fc4182b3944b1b36ca28@cweb013.nm&contentType=image/jpeg&filename=1747273018484.jpeg&org=1" alt="JARDIN 바로가기" /></a></p>
	</td>
</tr>
<tr>
	<td style="width:700px;height:50px;padding:0;vertical-align:top;font-size:0;line-height:0;text-align:center;">
		<img src="https://mail.naver.com/read/image/original/?mimeSN=1747273032.914716.170.34560&offset=1901&size=4757162&u=x_xitt&cid=ee8fce1a52921deee032a98f3633b271@cweb010.nm&contentType=image/jpeg&filename=1747273008237.jpeg&org=1" alt="" />
	</td>
</tr>
<tr>
	<td style="width:700px;height:140px;padding:0;margin:0;vertical-align:top;background-color:#5a524c;">
		<p style="width:620px;margin:20px 0 0 40px;padding:0;text-align:center;line-height:1.5;color:#b2aeac;">메일수신을 원치 않으시는 분은 로그인 후. <span style="color:#ffffff">메일 수신 여부</span>를 변경해주시기 바랍니다.<br/>IF YOU DO NOT WISH TO RECEIVE EMAILS FROM US, PLEASE LOG-IN AND UPDATE<br/> YOUR MEMBERSHIP INFORMATION.</p>

		<p style="width:620px;margin:15px 0 0 40px;padding:0;text-align:center;line-height:1.5;color:#b2aeac;"><span style="color:#ffffff">본 메일에 관한 문의사항은 사이트 내 고객센터를 이용해주시기 바랍니다.</span><br/>COPYRIGHT ©  2014 JARDIN ALL RIGHTS RESERVED.</p>
	</td>
</tr>
</table>



</div>
</body>
</html>
"""

# 정보

send = 'x_xitt@naver.com'
recv = ''
password = 'N77MXDMPGXSC'
smtp = 'smtp.naver.com'
smtp_port = 587


# 기본 이메일 발송 시 사용하는 모듈
from email.mime.text import MIMEText
import smtplib
# 파일 첨부시 사용하는 모듈
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


# MIME모듈 설정
msg = MIMEText(html,'html')
msg['From'] = send
msg['To'] = recv
msg['Subject'] = '임시 비밀번호 발급'

# 네이버 접속, 메일쓰기
s = smtplib.SMTP(smtp,smtp_port)
s.starttls()
s.login(send,password)
s.sendmail(send,recv,msg.as_string())
s.close()

print("발송 완")