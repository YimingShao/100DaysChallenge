from api import (get_info_by_zip,get_info_by_name,get_info_by_coor,status_print)
import requests.exceptions
import sys

def main():

    menu()
    key = ''
    while key is not '4':
        key=input_key()
        if key is '1':
            my_zip=input('Insert your zipcode(Only in U.S):\t')
            data = get_info_by_zip(zipcode=my_zip, country_code='us')
        elif key is '2':
            my_lat=input('Insert a latitude:\t')
            my_lon = input('Insert a longitude:\t')
            data = get_info_by_coor(lat=str(my_lat), lon=str(my_lon))
        elif key is '3':
            my_city=input('Insert a city name:\t')
            my_country=input('Insert a country code:\t')
            data = get_info_by_name(city=my_city, country=my_country)
        if data is not None:

            status_print(data)


    Quit()


def menu():
    print('''
    ----------Status Checker----------
    1. Check by zip code (U.S only)
    2. Check by coordinate
    3. Check by city, country name
    4. Quit
    ''')

def input_key():
    key = input('Your choice:\t')
    if key not in ['1','2','3','4']:
        print('Invalid input')
        return input_key()
    return key

def Quit():
    sys.exit('Thank you\t')


if __name__ == '__main__':
    main()