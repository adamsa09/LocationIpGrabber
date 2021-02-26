import requests
import smtplib
import ssl
import json

r = requests.get('https://ipinfo.io')
ipinfo = r.json()

port = 465

context = ssl.create_default_context()

input("Before we start, go to\nhttps://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4O13KGBUwF9HwEI0q6D634Jj7VWs9WEG4fnoJhshHctblM9kwofamyR0lqEjekUtfJ9PWn8O73_1ywEhFwVaYVhsV-_Pg\nand enable less secure apps. When finished, click enter in the console.")

sender_email = input('What is your gmail: ')
sender_password = input(
    'Enter your gmail password. If you are unsecure about typing it here feel free to view the source code: ')
recv_email = input('Where should I send the info (enter an email): ')

with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recv_email, ipinfo['ip'])
