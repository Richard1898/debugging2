#
# Uzdevums:
# Apvienojiet divas programmas. Atspoguļojiet laika apstākļus katrai stundai, pilsētai kuru ievada lietotājs.
# Pilsētas koordinātes paņemiet ar pirmo pieprasījumu (pirmu rezultātu) un laika apstākļus pieprasiet ar dotam koordinātem
#
import urllib.request
import json

def get_weather_information(weather):
    link = f"https://api.open-meteo.com/v1/forecast?latitude=56.8&longitude=24.2&hourly=temperature_2m,precipitation&forecast_days=1"
    
    with urllib.request.urlopen(link) as response:
        data = response.read().decode('utf-8')

    return json.loads(data)
def get_city_information(city):
    link = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=3&language=lv&format=json"
    
    with urllib.request.urlopen(link) as response:
        data = response.read().decode('utf-8')

    return json.loads(data)

def display_city_information(city_info):
    if city_info:
        print("City Information:")
        for city_data in city_info['results']:
            print(f"Name: {city_data['name']}")
            print(f"Country: {city_data['country']}")
            print(f"Latitude: {city_data['latitude']}")
            print(f"Longitude: {city_data['longitude']}")
            print(f"Population: {city_data['population']}")
            print(f"Timezone: {city_data['timezone']}")
            print(f"Country_code: {city_data['country_code']}")
            print("-----------------------")
            def display_city_information(weather_info):
                if weather_info:
                    print("Weather Information:")
                    for index in range(24):
                        print(f"Temperature: {weather_info['hourly']['temperature_2m'][index]}")
                        print(f"Precipitation: {weather_info['hourly']['precipitation'][index]}")
                        print("-----------------------")
    else:
        print("No city information available.")

weather_name = input("Enter city name: ")
if len(weather_name)>= 2:
    print("Correct")
else:
    print("Inncorrect try again")
    weather_name = input("Enter city name: ")
weather_information = get_weather_information(weather_name)
display_city_information(weather_information)
