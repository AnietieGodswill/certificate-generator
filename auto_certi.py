import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from PIL import Image, ImageDraw, ImageFont
def gen_cert():
    global sample_email,sample_name
    with open('sample_name.txt') as f:
        content = f.readlines()
        content = [x.strip() for x in content] #to remove whitespace
        font = ImageFont.truetype('arial.ttf',60)
        sample_name = []
        sample_email = []
        for i in content:
            s = i.split(',')
            sample_name.append(s[0])
            sample_email.append(s[1])
            sample_image = Image.open('sample_certi.png')
            draw = ImageDraw.Draw(sample_image)
            draw.text(xy=(450,350),text='{}'.format(s[0]),fill=(0,0,0),font=font)
            sample_image.save('certificates/{}.png'.format(s[0]))
        
def send_mail():
        for i,j in zip(sample_name,sample_email):
            email_user = 'Enter your email address'
            email_password = 'Enter your password'
            subject = 'Certificate Of Participation'
            msg = MIMEMultipart()
            msg['From'] = email_user
            msg['To'] = j
            msg['Subject'] = subject
            body = 'Hi there, sending this email from Python!'
            msg.attach(MIMEText(body,'plain'))
            filename = 'certificates/{}.png'.format(i)
            attachment  =open(filename,'rb')
            part = MIMEBase('application','octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',"attachment; filename= "+filename)
            msg.attach(part)
            text = msg.as_string()
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(email_user,email_password)
            server.sendmail(email_user,j,text)
            server.quit()  
gen_cert()
send_mail()