def recommend_hotel(data_hotel):
    counter = 1
    for hotels in data_hotel["data"]:
        price_level = hotels["price_level"]
        if price_level == None:
            price_level = "None"
        rating = hotels["rating"]
        if rating == None:
            rating = "None"
        print("{0} {1:<60}\t{2:<5}\t{3:<5}".format(counter,hotels["name"],rating,price_level))
        counter += 1

    hotel_choice = int(input("Where do you want to stay? "))
    return data_hotel["data"][hotel_choice-1]


def recommend_restaurant(data_restaurant):

    meals = {}
    for x in range(0, len(data_restaurant["data"])):
        name = data_restaurant["data"][x]["name"]
        print("{0:<3}.\t{1:<50}".format(x+1, name))

    x = int(input("Select restaurant number: "))

    if x-1 > len(data_restaurant["data"]):
        print("Game over")
        return 0;

    print("Selected: {}".format(data_restaurant["data"][x-1]["name"]) )
    print("   Price: {}".format(data_restaurant["data"][x-1]["price_level"]))
    for i in range(0, len(data_restaurant["data"][x-1]["cuisine"])):
        cuisine = data_restaurant["data"][x-1]["cuisine"][i]["localized_name"]
        print("    Cusine {0:<3}.\t{1:<50}".format(i+1, cuisine))
    return data_restaurant["data"][x-1]

def recommend_attraction(data_attraction):

    meals = {}
    for x in range(0, len(data_attraction["data"])):
        name = data_attraction["data"][x]["name"]
        print("{0:<3}\t{1:<50}".format(x+1, name))

    x = int(input("Select restaurant number: "))

    if x-1 > len(data_attraction["data"]):
        print("Game over")
        return 0;

    print("Selected: {}".format(data_attraction["data"][x-1]["name"]) )
    print("   Rating: {}".format(data_attraction["data"][x-1]["rating"]))
    for i in range(0, len(data_attraction["data"][x-1]["attraction_types"])):
        attraction_types = data_attraction["data"][x-1]["attraction_types"][i]["localized_name"]
        print("   Type  {0:<3}\t{1:<50}".format(i+1, attraction_types))
    return data_attraction["data"][x-1]
