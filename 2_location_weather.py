#
# Uzdevums:
# Izmantojot piemēru no pirma uzdevuma, izveidojiet programmu kas atspoguļos laika apstakļus (temperaturu un nokrišņus) pa stundām 
# izmantojot sekojošu datu linku 
# https://api.open-meteo.com/v1/forecast?latitude=56.8&longitude=24.2&hourly=temperature_2m,precipitation&forecast_days=1
import urllib.request
import json

def get_weather_information(weather):
    link = f"https://api.open-meteo.com/v1/forecast?latitude=56.8&longitude=24.2&hourly=temperature_2m,precipitation&forecast_days=1"
    
    with urllib.request.urlopen(link) as response:
        data = response.read().decode('utf-8')

    return json.loads(data)

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