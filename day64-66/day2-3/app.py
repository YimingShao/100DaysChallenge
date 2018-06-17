import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import  MIMEMultipart
from email.mime.text import MIMEText
import re
import sys
import os
from os.path import basename


def main():
    menu()
    key = rec_input()
    file_list=[]

    while key !='q':
        if key == 'l':
            file_list=list_files()
        elif key == 's':
            if len(file_list) == 0:
                print('Files are not ready!')
            else:
                select_file_to_send(file_list)
        key = rec_input()
    print('\nBye Bye!\n')
    sys.exit()


def rec_input():
    print()
    key = input('Insert your selection:\t')
    if key.lower() not in ['l', 's', 'q']:
        return rec_input()
    return key.lower()

def select_file_to_send(file_list):

    print('[A]dd files')
    print('[S]end files')

    choice = input('Insert your choice:\t').lower()
    send_list=[]

    while choice != 's':
        if choice not in ['s', 'a']:
            print('Invalid command!')
        elif choice == 'a':
            try:
                k = int(input('Add a file(the index):\t'))
            except ValueError:
                print('Not an integer!')
                continue

            if k < 0 or k > len(file_list)+1:
                print('Out of range')
            else:
                if file_list[k-1] in send_list:
                    print(f'file {file_list[k-1]} already added, try again')
                else:
                    send_list.append(file_list[k-1])
                    print(f'{send_list} are added')
        choice = input('Insert your choice:\t').lower()

    print()
    my_email = input_email()
    password = input('Insert your password:\t')
    to_add = my_email
    msg = MIMEMultipart()
    msg['From'] = my_email
    msg['To'] = to_add
    msg['Subject'] = input('Input your subject:\t')

    body = input('Input a text:\t')

    bcc = target_set()

    msg.attach(MIMEText(body, 'plain'))

    for f in send_list:
        with open(f, "rb") as fil:
            ext = f.split('.')[-1:]
            attachedfile = MIMEApplication(fil.read(), _subtype = ext)
            attachedfile.add_header(
                'content-disposition', 'attachment', filename=basename(f) )
        msg.attach(attachedfile)


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


def menu():
    print('---------------------')
    print('File emailer')
    print('[L]ist all files and ready to send')
    print('[S]end select files')
    print('[Q]uit')
    print('---------------------')

def list_files():
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    i=0
    for f in files:
        print(f'{i+1}. {f}')
    return files

def check_mail(mail):
    if (re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", mail)):
        return True
    return False


if __name__ == '__main__':
    main()