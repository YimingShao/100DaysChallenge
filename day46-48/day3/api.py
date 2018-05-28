import requests
import smtplib
import bs4


URL = "my_file.html"
sender = 'shaoyiminglobo@gmail.com'

def scrape():
    header_list = []

    soup = bs4.BeautifulSoup(open(URL).read(), 'html.parser')
    html_header_list = soup.select('.projectHeader')

    for headers in html_header_list:
        header_list.append(headers.getText())

    key = rec_input()
    if key is 'y':
        target=input('Input your email:\t')
        try:
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(sender,'shao1234')
            msg = convert_to_text(header_list)
            server.sendmail(sender, target, msg)
            server.quit()
        except Exception as x:
            print(x)

    for headers in header_list:
        print(headers)


def rec_input():
    key = input('Do you want to email to your self:(y/n)\t')
    if key not in ['y','n']:
        return rec_input()
    return key

def convert_to_text(list):
    return '\n'.join(list)