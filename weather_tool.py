import requests

def get_weather(city):

    cities = {
        "Delhi": (28.6139, 77.2090),
        "Mumbai": (19.0760, 72.8777),
        "Goa": (15.2993, 74.1240),
        "Bangalore": (12.9716, 77.5946),
        "Chennai": (13.0827, 80.2707),
        "Hyderabad": (17.3850, 78.4867),
        "Kolkata": (22.5726, 88.3639),
        "Jaipur": (26.9124, 75.7873)
    }

    city = city.strip().title()

    if city not in cities:
        return "Weather not found"

    latitude, longitude = cities[city]

    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

    response = requests.get(url)

    data = response.json()

    temperature = data["current_weather"]["temperature"]

    windspeed = data["current_weather"]["windspeed"]

    return f"Temperature: {temperature}°C, Wind Speed: {windspeed} km/h"

print(get_weather("kolkata"))