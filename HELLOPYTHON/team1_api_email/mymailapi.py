import smtplib
from email.mime.text import MIMEText

sendEmail = "interstellar1999@naver.com"
recvEmail = "interstellar1999@naver.com"
password = "네이버 비밀번호"

smtpName = "smtp.naver.com" #smtp 서버 주소
smtpPort = 587 #smtp 포트 번호

text = "매일 내용"
msg = MIMEText(text)
# MIMEText(text , _charset = "utf8")
# 주 유형 text의 MIME 객체를 만드는 데 사용
msg['Subject'] ="이것은 메일제목"
msg['From'] = sendEmail
msg['To'] = recvEmail
print(msg.as_string())

s=smtplib.SMTP( smtpName , smtpPort ) #메일 서버 연결
s.starttls() #TLS 보안 처리
s.login( sendEmail , password ) #로그인
s.sendmail( sendEmail, recvEmail, msg.as_string() ) #메일 전송, 문자열변환
s.close() #smtp 서버 연결을 종료합니다