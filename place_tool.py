import json


def get_places(city):

    with open("data/places.json", "r") as file:
        places = json.load(file)

    city_places = []

    for place in places:

        if place["city"].lower() == city.lower():

            city_places.append(place)

    return city_places


print(get_places("Delhi"))