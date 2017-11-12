from web_get import *
from UserPreferences import *
from recommend_algorithm import *


from pprint import pprint

if __name__ == "__main__":
	location = input("Where are you going? ")
	print("Getting TripAdvisor data for {}.".format(location))
	data_hotel = web_get_hotel(location)
	data_restaurant = web_get_restaurant(location)
	data_attraction = web_get_attraction(location)
	print("Done.")

	start_date = input("Please enter your start date mm dd yyyy: ")
	end_date = input("Please enter your end date mm dd yyyy: ")


	
	user = UserP([int(i) for i in start_date.split()], [int(i) for i in end_date.split()], location)

	
	choice = 1
	while choice != 4:
		print("1. Choose Hotel")
		print("2. Add a Meal to your Itinerary")
		print("3. Add an Event to your Itinerary")
		print("4. Print Itinerary")
		choice = int(input("Select an option: "))
			
		if choice == 1:
			# add wanted hotel
			hotel_choice = recommend_hotel(data_hotel)
			user.add_hotel_choice(hotel_choice)
		elif choice == 2:
			# add wanted restaurant
			day = input("What day of your trip are you adding a meal to? ")
			restaurant_choice = recommend_restaurant(data_restaurant)
			user.add_restaurant_choice(restaurant_choice, day)
		elif choice == 3:
			# add wanted attraction
			day = input("What day of your trip are you adding an event to? ")
			attraction_choice = recommend_attraction(data_attraction)
			user.add_attraction_choice(attraction_choice, day)
			
			
	
	
	
	
	
	
	
	
	
	
	
	