import json


def recommend_hotel(data_hotel):

	hotelsDictionary = {}
	hotelsIDs = {}
	for x in range(0, int(data_hotel["paging"]["results"])):
		if "ranking_data" in data_hotel["data"][x]:
			if data_hotel["data"][x]["ranking_data"] != None:
				if "ranking" in data_hotel["data"][x]["ranking_data"]:
					if data_hotel["data"][x]["ranking_data"]["ranking"] != None:
						ranking = int(data_hotel["data"][x]["ranking_data"]["ranking"])
						hotelsDictionary[ranking] = data_hotel["data"][x]["name"]
						hotelsIDs[ranking] = x+1
						
	counter = 1
	for keys in sorted(hotelsDictionary.keys()):
		if counter == 21:
			break
		print ("Hotel ID: {0:<2}\tRated: #{1:<4}\tName: {2:<50}".format(hotelsIDs[keys], keys, hotelsDictionary[keys]) )
		counter += 1
	print ()	
	hotel_choice = int(input("Select a hotel number: "))
	print("   Price: {}".format(data_hotel["data"][x-1]["price_level"]))
	
	print ()
	confirmation_number = int(input("Confirm Selection number or select again: "))
	
	while hotel_choice != confirmation_number:
		hotel_choice = confirmation_number
		
		print("   Price: {}".format(data_hotel["data"][x-1]["price_level"]))
		print ()
		confirmation_number = int(input("Confirm Selection number or select again: "))
	else:
		return data_hotel["data"][hotel_choice-1]


def recommend_restaurant(data_restaurant):

	print ("\n\n\n")
	restaurantsDictionary = {}
	restaurantsIDs = {}
	for x in range(0, int(data_restaurant["paging"]["results"])):
		if "ranking_data" in data_restaurant["data"][x]:
			if data_restaurant["data"][x]["ranking_data"] != None:
				if "ranking" in data_restaurant["data"][x]["ranking_data"]:
					if data_restaurant["data"][x]["ranking_data"]["ranking"] != None:
						ranking = int(data_restaurant["data"][x]["ranking_data"]["ranking"])
						restaurantsDictionary[ranking] = data_restaurant["data"][x]["name"]
						restaurantsIDs[ranking] = x+1
	
	
	counter = 1
	for keys in sorted(restaurantsDictionary.keys()):
		if counter == 21:
			break
		print ("Restaurant ID: {0:<2}\tRated: #{1:<4}\tName: {2:<50}".format(restaurantsIDs[keys], keys, restaurantsDictionary[keys]) )
		counter += 1
		
	print ()
	x = int(input("Select restaurant number: "))

	if x-1 > len(data_restaurant["data"]):
		print("Game over")
		return 0;

	print("Selected: {}".format(data_restaurant["data"][x-1]["name"]) )
	print("   Price: {}".format(data_restaurant["data"][x-1]["price_level"]))
	for i in range(0, len(data_restaurant["data"][x-1]["cuisine"])):
		cuisine = data_restaurant["data"][x-1]["cuisine"][i]["localized_name"]
		print("    Cusine {0:<3}.\t{1:<50}".format(i+1, cuisine))
	print ()
	y = int(input("Confirm Selection number or select again: "))
	
	while x != y:
		x = y

		if x-1 > len(data_restaurant["data"]):
			print("Game over")
			return 0;

		print("Selected: {}".format(data_restaurant["data"][x-1]["name"]) )
		print("   Price: {}".format(data_restaurant["data"][x-1]["price_level"]))
		for i in range(0, len(data_restaurant["data"][x-1]["cuisine"])):
			cuisine = data_restaurant["data"][x-1]["cuisine"][i]["localized_name"]
			print("    Cusine {0:<3}.\t{1:<50}".format(i+1, cuisine))
		print ()
		y = int(input("Confirm Selection number or select again: "))
		
	
	return data_restaurant["data"][x-1]
		
		


def recommend_attraction(data_attraction):

	print("\n\n\n")
	attractionsDictionary = {}
	attractionsIDs = {}
	for x in range(0, int(data_attraction["paging"]["results"])):
		if "ranking_data" in data_attraction["data"][x]:
			if data_attraction["data"][x]["ranking_data"] != None:
				if "ranking" in data_attraction["data"][x]["ranking_data"]:
					if data_attraction["data"][x]["ranking_data"]["ranking"] != None:
						ranking = int(data_attraction["data"][x]["ranking_data"]["ranking"])
						attractionsDictionary[ranking] = data_attraction["data"][x]["name"]
						attractionsIDs[ranking] = x+1
						
	
	
	counter = 1
	for keys in sorted(attractionsDictionary.keys()):
		if counter == 21:
			break
		print ("Attraction ID: {0:<2}\tRated: #{1:<4}\tName: {2:<50}".format(attractionsIDs[keys], keys, attractionsDictionary[keys]) )		
		counter += 1
		
	

	print ()
	x = int(input("Select Restaurant Number: "))

	if x-1 > len(data_attraction["data"]):
		print("Game over")
		return 0;

	print("Selected: {}".format(data_attraction["data"][x-1]["name"]) )
	print("   Rating: {}".format(data_attraction["data"][x-1]["rating"]))
	for i in range(0, len(data_attraction["data"][x-1]["attraction_types"])):
		attraction_types = data_attraction["data"][x-1]["attraction_types"][i]["localized_name"]
		print("   Type  {0:<3}\t{1:<50}".format(i+1, attraction_types))
		
	print ()	
	y = int(input("Confirm Selection Number or Reselect: "))
	
	while x != y:
		x = y

		if x-1 > len(data_attraction["data"]):
			print("Game over")
			return 0;

		print("Selected: {}".format(data_attraction["data"][x-1]["name"]) )
		print("   Rating: {}".format(data_attraction["data"][x-1]["rating"]))
		for i in range(0, len(data_attraction["data"][x-1]["attraction_types"])):
			attraction_types = data_attraction["data"][x-1]["attraction_types"][i]["localized_name"]
			print("   Type  {0:<3}\t{1:<50}".format(i+1, attraction_types))
		
		print ()
		y = int(input("Confirm Selection number or select again: "))
		
	
		
		
	return data_attraction["data"][x-1]
	
	
	
	
	
	
	
	
	
	
	
	
	