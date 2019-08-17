
# Requirements
# Create environment variable 
# NIT_USR : Your User Name in Nit mail server
# NIT_PW : Your mail server password
# MAIL_USR : Your gmail server username
# MAIL_PW : Your gmail server password
# MAIL_SND : To which mail the notification to send to


import smtplib, ssl, os
import requests
from bs4 import BeautifulSoup
import time
from apscheduler.schedulers.background import BackgroundScheduler
from email.message import EmailMessage

mgs = EmailMessage()
mgs['Subject'] = "NitRkl Web Mail!"
mgs['From'] = os.environ.get("MAIL_USR")
mgs['To'] = os.environ.get("MAIL_SND")

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
}
login_data ={
    'loginOp': 'login',
    'client': 'mobile',
}
login_data['username'] = os.environ.get("NIT_USR")
login_data['password'] = os.environ.get("NIT_PW")

def check4Unread(msg):
    if msg.find("span",{"class":"Img ImgEnvelope"}): return True
    return False
    
def sendmail(msg): 
    mgs.set_content(msg)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=context) as server:
        server.login(os.environ.get("MAIL_USR"), os.environ.get("MAIL_PW"))
        server.send_message(mgs)

        
def webscrape():
    with requests.Session() as s:
        url = "https://mail.nitrkl.ac.in/"
        r= s.get(url,headers=headers)
        soup = BeautifulSoup(r.content,features="html.parser")
        login_data["login_csrf"] = soup.find('input',attrs={'name':'login_csrf'})['value']
        
        r= s.post(url,data=login_data,headers=headers)
        soup = BeautifulSoup(r.content)
        inbox = soup.find("div", {"id": "dlist-view"})
        message_list =list(filter(check4Unread,inbox.find_all("div",{"class":"tbl"})))
        info = ""
        for msg in message_list:
            mg ="Form: {}\nTitle: {}\nContent: {}\n\n".format(msg.a.text.strip(),
                            msg.find("div",{"class":"sub-span"}).text.strip(),
                            msg.find("div",{"class":"frag-span small-gray-text"}).text.strip())
            info = info + mg
        print(info)
        if len(message_list) > 0:
            message ="""https://mail.nitrkl.ac.in\n""" + info
            sendmail(message )
            print("mail sent!")

if __name__ == "__main__":
    scheuler = BackgroundScheduler()
    scheuler.add_job(webscrape,'interval',minutes=20)
    scheuler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()




