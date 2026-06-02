import json

def search_hotels(city):

    with open("data/hotels.json", "r") as file:
        hotels = json.load(file)

    results = []

    for hotel in hotels:

        if hotel["city"].lower() == city.lower():
            results.append(hotel)

    if len(results) == 0:
        return "No hotels found"

    cheapest = min(results, key=lambda x: x["price_per_night"])

    return cheapest


print(search_hotels("Goa"))