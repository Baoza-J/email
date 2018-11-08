from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

def make_msg():
    email = MIMEMultipart('alternative')
    text = MIMEText('Hello world!\r\n', 'plain')
    email.attach(text)
    html = MIMEText(
                    '<html><body><h4>Hello World!</h4>'
                    '</body></html>', 'html')
    email.attach(html)
    return email

def make_img():
    fn = input('输入图片带后缀的名称')
    f = open(fn,'r')
    date = f.read()
    f.close()
    email = MIMEImage(data, name=fn)
    email.add_header('Content-Disposition', 'attachment; filename="%s"' % fn)
    return email

def send_msg_mail():
    sender = input('输入发送方的邮件地址')
    receiver = input('输入接收方的邮件地址')
    psw = input('输入发送方的授权码')
    s = SMTP('smtp.163.com')
    s.login(sender, psw)
    m = make_msg()
    m['From'] = sender
    m['To'] = receiver
    m['Subject'] = 'python 学习邮件'
    s.sendmail(sender, receiver, m.as_string())

def send_img_mail():
    sender = input('输入发送方的邮件地址')
    receiver = input('输入接收方的邮件地址')
    psw = input('输入发送方的授权码')
    s = SMTP('smtp.163.com')
    s.login(sender, psw)
    i = make_img()
    i['From'] = sender
    i['To'] = receiver
    i['Subject'] = 'python 学习邮件'
    s.sendmail(sender, receiver, m.as_string())

if __name__ == '__main__':
    while 1:
        t = input('输入文件类型，m for message，i for image, q for quit') 
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
            print('please try again')
