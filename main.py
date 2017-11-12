from web_get import *
from UserPreferences import *
from recommend_algorithm import *

from pprint import pprint

if __name__ == "__main__":

# example of using multi_get
    '''
        ids = ["89575","233835","192416"]
        data = multi_get.multi_get(ids)
        print(data.text)
    '''

    location = input("Where are you going? ")
    start_date = input("Enter the data you are available from (mm/dd/yyyy): ")
    end_date = input("Enter the data you are available until (mm/dd/yyyy): ")

    data_hotel = web_get_hotel(location)
    data_restaurant = web_get_restaurant(location)
    data_attraction = web_get_attraction(location)

    user = UserP(start_date, end_date, location)

    # add wanted hotel
    hotel_choice = recommend_hotel(data_hotel)
    user.add_hotel_choice(hotel_choice)

    # add wanted restaurant
    restaurant_choice = recommend_restaurant(data_restaurant)
    user.add_restaurant_choice(restaurant_choice)

    # add wanted attraction
    attraction_choice = recommend_attraction(data_attraction)
    user.add_attraction_choice(attraction_choice)
