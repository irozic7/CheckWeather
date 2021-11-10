from pprint import pprint
from urllib.request import urlopen
import json
import csv

def cityy(city, csv_writer):
    
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=9fd4a33e0db32b96a20241175b963165&units=metric'.format(city)

    request = urlopen(url)
    text = request.read().decode('utf-8')
    data = json.loads(text)

    # pprint(data)

    cityy = data['name']
    countryy = data['sys']['country']
    weatherr = data['weather'][0]['description']
    temperaturee = data['main']['temp']
    wind_speedd = data['wind']['speed']
    print('-City: ', cityy)
    print('-Country: ', countryy)

    for weather in data['weather']:
        shortdesc = weather['main']
        print("-Short Description: ", shortdesc)

    print('-Accurate Description: ', weatherr)
    print('-Temperature: {} °C'.format(temperaturee))
    print('-Wind speed: {} m/s'.format(wind_speedd))

    csv_writer.writerow([cityy, countryy, shortdesc, weatherr, temperaturee, wind_speedd])

def main():
    with open('weather_data.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["City", "Country", "Short description", "Accurate description", "Temperature", "Wind Speed"])

        while True:
            print('\n Check the weather')
            city = input('\n Input any city in the world: ')
            cityy(city, csv_writer) #pozove def cityy
            url2 = 'http://api.openweathermap.org/data/2.5/weather?q={}&mode=html&appid=9fd4a33e0db32b96a20241175b963165'.format(city)
            print('\n Link:  ', url2)
            
            restart = input('\n Wanna check another city? yes/no ').lower()
            if restart == 'yes':
                continue
            else:
                
                print("\n      Thank you for your time! ")
                
                
                break

main()