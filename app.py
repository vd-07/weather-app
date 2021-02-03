# coding: utf-8
# Your code here!
import requests

def check_woeid(city_name):
    url = "https://www.metaweather.com/api/location/search/?query=" + city_name

    response = requests.get(url)

    if response.json():

        woeid = response.json()[0]['woeid']

        return woeid

    print("No city found\nBangalore")

    return check_woeid("bangalore")

    

def check_weather(woeid):
    url = "https://www.metaweather.com/api/location/" + str(woeid)

    response = requests.get(url)

    return  response.json()['consolidated_weather'][0]['weather_state_name']

# Main app

city_name = input("Enter any city name : ")

woeid = check_woeid(city_name)

# print(response.json()[0])

# print(response.text)

print("Today's weather is : " + check_weather(woeid))