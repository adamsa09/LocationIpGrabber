import requests
import smtplib
import ssl
import os
import json
from sys import argv, exit
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

if len(argv) < 2:
    print('-i   Get IP address\n-h   Get hostname\n-c   Get city\n-r   Get region\n-co  Get country\n-l   Get location (long, lat)\n-o   Organizion\n-p   Postal\n-t   Timezone\n-a   All Info')
    exit()

print('Loading...')
r = requests.get('https://ipinfo.io')
ipinfo = r.json()
os.system('cls')


def findinfo():
    msg = ''
    if '-i' in argv:
        msg = msg + 'IP ' + ipinfo['ip'] + ','
    if '-h' in argv:
        msg = msg + 'HOSTNAME ' + ipinfo['hostname'] + ','
    if '-c' in argv:
        msg = msg + 'CITY ' + ipinfo['city'] + ','
    if '-r' in argv:
        msg = msg + 'REGION ' + ipinfo['region'] + ','
    if '-co' in argv:
        msg = msg + 'COUNTRY ' + ipinfo['country'] + ','
    if '-l' in argv:
        msg = msg + 'LATITUDE, LONGITUDE LOCATION ' + ipinfo['loc'] + ','
    if '-o' in argv:
        msg = msg + 'ORGANIZATION ' + ipinfo['org'] + ','
    if '-t' in argv:
        msg = msg + 'TIMEZONE ' + ipinfo['timezone'] + ','

    return msg


port = 465


context = ssl.create_default_context()

input("Before we start, go to\nhttps://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4O13KGBUwF9HwEI0q6D634Jj7VWs9WEG4fnoJhshHctblM9kwofamyR0lqEjekUtfJ9PWn8O73_1ywEhFwVaYVhsV-_Pg\nand enable less secure apps. When finished, click enter in the console.")

sender_email = input('What is your gmail: ')
sender_password = input(
    'Enter your gmail password. If you are unsecure about typing it here feel free to view the source code: ')
recv_email = input('Where should I send the info (enter an email): ')
message = findinfo()
subject = input("Subject: ")
msg = MIMEMultipart()
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = recv_email
msg.attach(MIMEText(message))


with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recv_email, msg.as_string())
