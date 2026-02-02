from datetime import datetime
import webbrowser as web
import requests
from dotenv import load_dotenv
import os

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")


greet_messages=["hi","hello","hey","hi there","hey there"]
date_msgs=["what is the date today", "date", "tell me the date"]
time_msgs=["what is the time today", "time", "tell me the time"]


def get_location():
    response=requests.get("http://ip-api.com/json/")
    data=response.json()
    city=data.get("city","unknown location")
    country=data.get("country","unknown location")
    return country,city


def get_news():
    response = requests.get(f"https://newsapi.org/v2/everything?q=india&language=en&sortBy=publishedAt&apiKey={NEWS_API_KEY}")
    data = response.json()
    return data.get("articles", [])
    
def get_current_temperature():
    try:
        response = requests.get("http://ip-api.com/json/")
        data = response.json()
        lat = data.get("lat")
        lon = data.get("lon")
        weather_api_key = "c80edaca2ec8061c97958dbf4adb4944"
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_api_key}&units=metric"
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()
        temperature = weather_data['main']['temp']
        return temperature
    except:
        return None

chat=True
while chat:
    msg=input("Enter your message: ").lower()
    if msg in greet_messages:
        print("Hello how are you?")
    elif msg in date_msgs:
        print(datetime.now().date().strftime("%d-%m-%Y"))
    elif msg in time_msgs:
        current_time=datetime.now().time()
        print(current_time.strftime("%I:%M:%S"))
    elif "open" in msg :
        site=msg.split("open ")[-1]
        web.open(f"https://www.{site}.com/")
        print(f"Opening {site}")
    elif "calculate" in msg:
        m=msg.split()[-1]
        result=eval(m)
        print(result)
    elif "location" in msg:
        country,city= get_location()
        print(f"Your location is {city}, {country}")
     
    elif "news" in msg:
        news = get_news()
        if not news:
            print("No news available right now.")
        else:
            print("Top India-related news 🇮🇳:\n")
            for i in range(5):
                print(f"{i+1}. {news[i].get('title', 'No title')}")
    elif "weather" in msg:
        temperature = get_current_temperature()
        if temperature is not None:
            print(f"The current temperature is {temperature}°C")
        else:
            print("Could not retrieve the temperature at this time.")
    elif msg=="bye":
        chat=False
    else:
        print("I can't understand")

