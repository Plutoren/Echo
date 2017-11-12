class UserP:
    def __init__(self, start, location, end):
        self.start = start
        self.end = end
        self.location = location
        self.hotel_choice = []
        self.restaurant_choice = []
        self.attraction_choice = []
        self.schedule = []

    def add_hotel_choice(self,hotel):
        self.hotel_choice.append(hotel)

    def add_restaurant_choice(self,restaurant):
        self.restaurant_choice.append(restaurant)

    def add_attraction_choice(self,attraction):
        self.attraction_choice.append(attraction)
