from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
import smtplib

def make_msg():
    email = MIMEMultipart('alternative')
    print()
    textm = input('输入你想要发送的内容\n')
    textm += '\r\n'
    text = MIMEText(textm, 'plain')
    email.attach(text)
    htmlm = '<html><body><h4>' + textm + '</h4>'
    html = MIMEText(
                    htmlm + '</body></html>', 'html')
    email.attach(html)
    return email

def make_img():
    email = MIMEMultipart('related')
    content = MIMEText('<html><body><img src="cid:imaged" alt="imageid"></body></html>', 'html','utf-8')
    email.attach(content)
    print()
    fn = input('输入图片带后缀的名称\n')
    f = open(fn,'rb')
    data = f.read()
    f.close()
    img = MIMEImage(data)
    img.add_header('Content-ID', 'imageid') 
    #img.add_header('Content-Disposition', 'attachment; filename="%s"' % fn)
    email.attach(img)
    #return email

def send_msg_mail():
    print()
    sender = input('输入发送方的邮件地址\n')
    print()
    receiver = input('输入接收方的邮件地址\n')
    print()
    psw = input('输入发送方的授权码\n')
    print('稍等')
    s = SMTP('smtp.163.com')
    s.login(sender, psw)
    m = make_msg()
    m['From'] = sender
    m['To'] = receiver
    print()
    subject = input('输入邮件标题\n')
    m['Subject'] = subject 
    s.sendmail(sender, receiver, m.as_string())

def send_img_mail():
    sender = 'huotiandayou121111@163.com'
    receivers = '13522922570@163.com'
    message =  MIMEMultipart('related')
    subject = '终于能发图片了'
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = receivers
    content = MIMEText('<html><body><img src="cid:imageid" alt="imageid"></body></html>','html','utf-8')
    message.attach(content)

    file=open("1.jpg", "rb")
    img_data = file.read()
    file.close()

    img = MIMEImage(img_data)
    img.add_header('Content-ID', 'imageid')
    message.attach(img)

    try:
        server=SMTP("smtp.163.com")
        server.login(sender,"121212WJ")
        server.sendmail(sender,receivers,message.as_string())
        server.quit()
        print ("邮件发送成功")
    except smtplib.SMTPException as e:
        print(e)

if __name__ == '__main__':
    while 1:
        t = input('输入邮件类型，m 是文本，i 是图片, q 是退出\n') 
        t = t.lower()
        if t == 'm':
            send_msg_mail()
            break

        elif t == 'i':
            send_img_mail()
            break

        elif t == 'q':
            break
        else:
            print()
            print('please try again\n')
