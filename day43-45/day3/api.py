from datetime import datetime
import requests
import webbrowser

API_Zip_Code="http://api.openweathermap.org/data/2.5/weather?zip={},{}&appid={}"
API_City_Name="http://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}"
API_Coor="http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}"
API_KEY = "53c4a2755dc4cb6af684b4a08db10a6f"


def get_info_by_zip(zipcode, country_code):
    try:
        data = requests.get(API_Zip_Code.format(zipcode,country_code,API_KEY))
    except Exception as x:
        print(x)
        data=None
    return data

def get_info_by_name(city, country):
    try:
        data = requests.get(API_City_Name.format(city, country, API_KEY))
    except Exception as x:
        print(x)
        data=None
    return data

def get_info_by_coor(lat, lon):
    try:
        # data = requests.get(API_Coor.format(lat, lon, API_KEY))
        data=requests.get(API_Coor.format(lat, lon, API_KEY))
    except Exception as x:
        print(x)
        data=None
    return data

def status_print(data):
    try:
        data.raise_for_status()
        my_list = data.json()

        if my_list.get('name') is '':
            Location_name = 'Unknown'

        else:
            Location_name = my_list.get('name')
            Location_coor = f"lon: {my_list.get('coord').get('lon')}, lat: {my_list.get('coord').get('lat')}"
            Weather = my_list.get('weather')[0]['main']
            Weather_description = my_list.get('weather')[0]['description']
            temp = my_list.get('main')['temp']
            print('Place name: {}\ncoordinate: {}\nWeather: {}, {}\nTemperature: {}\n'.
                  format(Location_name, Location_coor, Weather, Weather_description, temp))
    except Exception as x:
        print(x)

def view_raw_data(city, country):
    try:
        webbrowser.open(API_City_Name.format(city, country, API_KEY), new=2)
    except Exception as x:
        print(x)


if __name__ == '__main__':
    view_raw_data('London', 'uk')