from tools.flight_tool import search_flights
from tools.hotel_tool import search_hotels
from tools.weather_tool import get_weather
from tools.place_tool import get_places


def travel_agent(source, destination):

    flight = search_flights(source, destination)

    hotel = search_hotels(destination)

    weather = get_weather(destination)

    places = get_places(destination)

    return {
        "flight": flight,
        "hotel": hotel,
        "weather": weather,
        "places": places[:3]
    }


   