from flask import Flask, render_template
# for getting full paths to attachements
import os
# for encoding messages in base64
from base64 import urlsafe_b64encode
# for dealing with attachement MIME types
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from mimetypes import guess_type as guess_mime_type

from team1_api_email.common import our_email, gmail_authenticate  

app = Flask(__name__)

# mail_info = ["coffee357722@gmail.com", "이메일 제목", "이메일 본문"]
mail_info = ["coffee357722@gmail.com", "도시락", "아 조금만 더 자고 싶은", "Tulips.jpg", "test.txt"]

@app.route('/')
@app.route('/send_email')
def show_send_mail():
    return render_template('index.html', mail=mail_info)

# Adds the attachment with the given filename to the given message
def add_attachment(message, filename):
    content_type, encoding = guess_mime_type(filename)
    if content_type is None or encoding is not None:
        content_type = 'application/octet-stream'
    main_type, sub_type = content_type.split('/', 1)
    if main_type == 'text':
        fp = open(filename, 'rb')
        msg = MIMEText(fp.read().decode(), _subtype=sub_type)
        fp.close()
    elif main_type == 'image':
        fp = open(filename, 'rb')
        msg = MIMEImage(fp.read(), _subtype=sub_type)
        fp.close()
    elif main_type == 'audio':
        fp = open(filename, 'rb')
        msg = MIMEAudio(fp.read(), _subtype=sub_type)
        fp.close()
    else:
        fp = open(filename, 'rb')
        msg = MIMEBase(main_type, sub_type)
        msg.set_payload(fp.read())
        fp.close()
    filename = os.path.basename(filename)
    msg.add_header('Content-Disposition', 'attachment', filename=filename)
    message.attach(msg)

def build_message(destination, obj, body, attachments=[]):
    if not attachments: # no attachments given
        message = MIMEText(body)
        message['to'] = destination
        message['from'] = our_email
        message['subject'] = obj
    else:
        message = MIMEMultipart()
        message['to'] = destination
        message['from'] = our_email
        message['subject'] = obj
        message.attach(MIMEText(body))
        for filename in attachments:
            add_attachment(message, filename)
    return {'raw': urlsafe_b64encode(message.as_bytes()).decode()}

def send_message(service, destination, obj, body, attachments=[]):
    return service.users().messages().send(
      userId="me",
      body=build_message(destination, obj, body, attachments)
    ).execute()


# send_emails
if __name__ == "__main__":
    # import argparse
    # parser = argparse.ArgumentParser(description="Email Sender using Gmail API")
    # parser.add_argument('destination', type=str, help='The destination email address')
    # parser.add_argument('subject', type=str, help='The subject of the email')
    # parser.add_argument('body', type=str, help='The body of the email')
    # parser.add_argument('-f', '--files', type=str, help='email attachments', nargs='+')
    #
    # args = parser.parse_args()
    app.run(debug=True)
    service = gmail_authenticate()
    # send_message(service, args.destination, args.subject, args.body, args.files)

    # test send email
    # send_message(service, "coffee357722@gmail.com", "이메일 api 테스트", 
    #             "이메일 api 테스트입니다.", ["test.txt", "credentials.json"])
    
    # send_message(service, "coffee357722@gmail.com", "이메일 api 테스트 - 첨부파일 없음", 
    #             "첨부파일 없는 이메일 api 테스트입니다.")
    
    # send_message(service, "coffee357722@gmail.com", "이메일 api 테스트 - 이미지", 
    #             "이미지 첨부파일 이메일 api 테스트입니다.", ["Tulips.jpg"])
    
    # send_message(service, "cjsrnk92@gmail.com", "이메일 api 테스트 - 삭제", 
    #             "삭제할 이메일 api 테스트입니다.", ["Tulips.jpg", "test.txt"])
    
    if len(mail_info) > 3 :
        atch = []
        for i in range(3, len(mail_info)) :
            atch.append(mail_info[i])
    
        send_message(service, mail_info[0], mail_info[1], mail_info[2], atch)

    else :
        send_message(service, mail_info[0], mail_info[1], mail_info[2])
    
    
    
