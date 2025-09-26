import os
from dotenv import load_dotenv
import requests
from django.shortcuts import render

load_dotenv()

def get_weather(request):
    city = request.GET.get('city', 'Delhi')
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()
    print(data)  # Debugging

    if data.get("cod") != 200:
        context = {"error": f"'{city}' city not found! Please enter correct spelling."}
    else:
        context = {
    "city": city,
    "temperature": data['main']['temp'],
    "description": data['weather'][0]['description'],
    "humidity": data['main']['humidity'],
    "wind_speed": data['wind']['speed'],
}

    
    return render(request, 'weather.html', context)

