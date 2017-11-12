
from datetime import date
from datetime import timedelta  
  

class UserP:
	def __init__(self, start_date, end_date, location):
		self.location = location
		self.start   = date(int(start_date[2]), int(start_date[0]), int(start_date[1]) )
		self.end = date(int(end_date[2]),   int(end_date[0]),   int(end_date[1])   )
		self.numberOfDays = self.end - self.start
		print ("Days traveling: {}".format(self.numberOfDays.days) )
		
		
		self.hotel_choice = []
		
		# Create dictionaries to store the user itinerary values
		self.restaurant_choice = {}
		self.attraction_choice = {}
		
		# Create lists for each day for meal and event choices
		for x in range(0, self.numberOfDays.days):
			self.restaurant_choice[x] = []
			self.attraction_choice[x] = []

	def add_hotel_choice(self,hotel):
		self.hotel_choice.append(hotel)

	def add_restaurant_choice(self,restaurant,day):
		if int(day) > self.numberOfDays.days:
			print("You are only traveling for {} days".format(self.numberOfDays.days))
			return 0
		#Add days
		date = self.start + timedelta(days=int(day)) 
		self.restaurant_choice[int(day)-1].append(restaurant)

	def add_attraction_choice(self,attraction,day):
		if int(day) > self.numberOfDays.days:
			print("You are only traveling for {} days".format(self.numberOfDays,days))
			return 0
		#Add days
		date = self.start + timedelta(days=int(day)) 
		self.attraction_choice[int(day)-1].append(attraction)