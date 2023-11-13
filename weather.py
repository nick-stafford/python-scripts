# check weather - never finished this
import requests

API_KEY = "your_api_key"  # get from openweathermap

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"
    # r = requests.get(url)
    # return r.json()
    pass

# print(get_weather("Seattle"))
