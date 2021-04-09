from datetime import date
import smtplib, ssl
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



port = "587"
smtp_server = "server"
me = "kontakt@technologic.org.pl"
you = "test@gmail.com"
password = "test"

file1 = open('lista.txt', 'r')
Lines = file1.readlines()
count = 0
today = date.today()
endday = date(2021, 4, 17)
#print (today)

delta = endday - today
#print (delta)
#exit (0)
# Strips the newline character
for line in Lines:
    s = line.split()
    dokogo = str(s[3]);
    print (dokogo)
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "BNI Masters - Arkusz Gains"
    msg['From'] = me
    msg['To'] = dokogo
    # chars.encode('utf-8')
    text ="Witam "+s[0]+",\nJak pewnie Ci wiadomo\n\nPozostało "+str(delta.days)+" dni\nW razie pytań jak zrobić arkusz nwww.technologic.org.pl\nkontakt@technologic.org.pl\n"
    print (text)
    html = f"""\
    <html>
     <head></head>
     <body>
      <p>Witam {s[0]},<br>
       Jak pewnie Ci wiadomo potrzebuję Twojego arkusza Gains.<br>
       www.technologic.org.pl<br>
       kontakt@technologic.org.pl<br>
      </p>
     </body>
    </html>
    """
    part1 = MIMEText(text,"plain", "utf-8")
    part2 = MIMEText(html, 'html')

    msg.attach(part1)
    msg.attach(part2)
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(me, password)
        server.sendmail(me, str(s[3]), msg.as_string())
