import smtplib
from email.mime.multipart import  MIMEMultipart
from email.mime.text import MIMEText
import re


def main():
    my_email = input_email()
    password = input('Insert your password:\t')
    to_add = my_email
    msg = MIMEMultipart()
    msg['From'] = my_email
    msg['To'] = to_add
    msg['Subject'] = input('Input your subject:\t')

    body = input('Input a text')

    bcc = target_set()

    msg.attach(MIMEText(body, 'plain'))
    smpt_server = smtplib.SMTP('smtp.gmail.com', 587)
    smpt_server.ehlo()
    smpt_server.starttls()

    smpt_server.login(my_email,password)
    text = msg.as_string()
    smpt_server.sendmail(my_email,[to_add]+bcc, text)




def input_email(key='your'):
    my_mail = input(f'Insert {key} email:\t')
    if not check_mail(my_mail):
        print('Invalid address')
        return input_email()
    return my_mail


def target_set():
    mail_set = set()
    print("\nEnter an email that you want to send, 'end' to stop entering:")
    while True:
        e = input('Enter an email:\t')
        if e == "end":
            break
        if not check_mail(e):
            print(f'{e} is not an invalid address')
        else:
            mail_set.update(e)
    return list(mail_set)




def check_mail(mail):
    if (re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", mail)):
        return True
    return False


if __name__ == '__main__':
    main()