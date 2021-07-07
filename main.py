import requests
from pprint import pprint

API_KEY = 'e8587f428732aeba63a3e4183a9837ff'

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_KEY+ "&q=" + city

weather_info = requests.get(base_url).json()

pprint(weather_info)
