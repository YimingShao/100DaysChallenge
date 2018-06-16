import smtplib

from_addr = 'shaoyiminglobo@gmail.com'
to_addr = 'shaoyiminglobo@gmail.com'

body = """New Releases and Sales on Steam
    
Click the links below to check them out!
   
"""

smtp_server = smtplib.SMTP('smtp.gmail.com', 587)

smtp_server.ehlo()

smtp_server.starttls()

smtp_server.login(' shaoyiminglobo@gmail.com ', ' shao1234 ')

smtp_server.sendmail(from_addr, to_addr, body)

smtp_server.quit()

print('Email sent successfully')
