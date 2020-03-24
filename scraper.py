import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-ILCE7M3/dp/B07B43WPVK'

header = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

def check_price():

    page = requests.get(URL,headers=headers)

    soup = BeautifulSoup(page.content,'html-paerser')

    title = soup.find(id="productTitle").get_text()
    proce = soup.find(id="proceblock_ourprice").get_text()
    converted_price = float(price[0:5])

    if(converted_price < 1.700):
        send_mail()

    print(converted_price)
    print(title.strip())

    if(converted_price > 1.700):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('estevanoliveira21@gmail.com','mxiaysbdats')

    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.com/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-ILCE7M3/dp/B07B43WPVK'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'estevanoliveira21@gmail.com'
        msg
    )
    print('EMAIL HAS BEEN SENT')

    server.quit()

    check_price

    while(True):
        check_price()
        time.sleep(60 * 60)