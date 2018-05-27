import api
import requests.exceptions
import sys
import webbrowser

def main():
    menu()
    key = ''
    while key is not '5':
        key=input_key()
        if key is '1':
            my_zip=input('Insert your zipcode(Only in U.S):\t')
            data = api.get_info_by_zip(zipcode=my_zip, country_code='us')
        elif key is '2':
            my_lat=input('Insert a latitude:\t')
            my_lon = input('Insert a longitude:\t')
            data = api.get_info_by_coor(lat=str(my_lat), lon=str(my_lon))
        elif key is '3':
            my_city=input('Insert a city name:\t')
            my_country=input('Insert a country code:\t')
            data = api.get_info_by_name(city=my_city, country=my_country)
        elif key is '4':
            my_city=input('Insert a city name:\t')
            my_country=input('Insert a country code:\t')
            api.view_raw_data(my_city,my_country)
            data= None
        if data is not None:
            api.status_print(data)

    Quit()


def menu():
    print('''
    Note: Do not send requests more than 60 times per minuet
    ----------Status Checker----------
    1. Check by zip code (U.S only)
    2. Check by coordinate
    3. Check by city, country name
    4. View raw data in browser
    5. Quit
    ''')

def input_key():
    key = input('Your choice:\t')
    if key not in ['1','2','3','4','5']:
        print('Invalid input')
        return input_key()
    return key

def Quit():
    sys.exit('Thank you\t')


if __name__ == '__main__':
    main()