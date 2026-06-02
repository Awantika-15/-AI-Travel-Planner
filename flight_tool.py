import json

def search_flights(source, destination):

    print("SOURCE:", source)
    print("DESTINATION:", destination)

    with open("data/flights.json", "r") as file:
        flights = json.load(file)

    results = []

    for flight in flights:

        print(flight["from"], "->", flight["to"])

        if (
            flight["from"].lower().strip() == source.lower().strip()
            and flight["to"].lower().strip() == destination.lower().strip()
        ):
            results.append(flight)

    if len(results) == 0:
        return "No flights found"

    return min(results, key=lambda x: x["price"])


print(search_flights("Delhi", "Kolkata"))