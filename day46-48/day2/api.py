import requests
import bs4

URL = "my_file.html"


def scrape():
    header_list = []

    soup = bs4.BeautifulSoup(open(URL).read(), 'html.parser')
    html_header_list = soup.select('.projectHeader')

    for headers in html_header_list:
        header_list.append(headers.getText())

    for headers in header_list:
        print(headers)