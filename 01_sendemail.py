from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

def make_msg():
    email = MIMEMultipart('alternative')
    print()
    textm = input('输入你想要发送的内容\n')
    textm += textm + '\r\n'
    text = MIMEText(textm, 'plain')
    email.attach(text)
    htmlm = '<html><body><h4>' + textm 
    html = MIMEText(
                    htmlm+'</body></html>', 'html')
    email.attach(html)
    return email

def make_img():
    print()
    fn = input('输入图片带后缀的名称\n')
    f = open(fn,'rb')
    data = f.read()
    f.close()
    email = MIMEMultipart('related')
    content = MIMEText('<html><body><img src="cid:imageid" alt="imageid"></body></html>','html','utf-8')
    email.attach(content)
    img = MIMEImage(data, name=fn)
    img.add_header('Content-ID', 'imageid')
    email.attach(img)
    return email

def send_msg_mail():
    print()
    sender = input('输入发送方的邮件地址\n')
    print()
    receiver = input('输入接收方的邮件地址\n')
    psw = input('输入发送方的授权码\n')
    print()
    s = SMTP('smtp.163.com')
    s.login(sender, psw)
    m = make_msg()
    m['From'] = sender
    m['To'] = receiver
    print()
    subject = input('请输入邮件标题\n')
    m['Subject'] = subject
    s.sendmail(sender, receiver, m.as_string())

def send_img_mail():
    print()
    sender = input('输入发送方的邮件地址\n')
    print()
    receiver = input('输入接收方的邮件地址\n')
    print()
    psw = input('输入发送方的授权码\n')
    s = SMTP('smtp.163.com')
    s.login(sender, psw)
    i = make_img()
    i['From'] = sender
    i['To'] = receiver
    print()
    subject = input('请输入邮件标题\n')
    i['Subject'] = subject
    s.sendmail(sender, receiver, i.as_string())

if __name__ == '__main__':
    while 1:
        print()
        t = input('输入文件类型，m for message，i for image, q for quit\n') 
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
            print('please try again\n')
