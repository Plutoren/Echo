
from datetime import date
from datetime import timedelta  
import calendar

class UserP:
	def __init__(self, start_date, end_date, location):
		self.location = location
		self.start = date(int(start_date[2]), int(start_date[0]), int(start_date[1]) )
		self.end = date(int(end_date[2]),   int(end_date[0]),   int(end_date[1])   )
		self.numberOfDays = self.end - self.start
		print ("Days traveling: {}".format(self.numberOfDays.days) )
		
		
		self.hotel_choice = []
		
		# Create dictionaries to store the user itinerary values
		self.restaurant_choice = {}
		self.attraction_choice = {}
		
		# Create lists for each day for meal and event choices
		for x in range(1, self.numberOfDays.days+1):
			self.restaurant_choice[x] = []
			self.attraction_choice[x] = []

	def add_hotel_choice(self,hotel):
		self.hotel_choice.append(hotel)

	def add_restaurant_choice(self,restaurant,day):
		if int(day) > self.numberOfDays.days:
			print("You are only traveling for {} days".format(self.numberOfDays.days))
			return 0
			
		if "hours" in restaurant:
			
			if restaurant["hours"] != None:
				if "week_ranges" in restaurant["hours"]:
				
					if len(restaurant["hours"]["week_ranges"]) >= int((self.start + timedelta(days=int(day)-1)).weekday()):
						
						if "times" in restaurant["hours"]["week_ranges"][int((self.start + timedelta(days=int(day)-1)).weekday())]:
							
							if restaurant["hours"]["week_ranges"][int((self.start + timedelta(days=int(day)-1)).weekday())+1]["times"] == []:
								print("Sorry but that restaurant is closed on {}s".format(calendar.day_name[(self.start + timedelta(days=int(day)-1)).weekday()]))
								return 0
							else:
								print (restaurant["hours"]["week_ranges"][int((self.start + timedelta(days=int(day)-1)).weekday())+1]["times"])
		#Add days
		date = self.start + timedelta(days=int(day)) 
		self.restaurant_choice[int(day)].append(restaurant)

	def add_attraction_choice(self,attraction,day):
		if int(day) > self.numberOfDays.days:
			print("You are only traveling for {} days".format(self.numberOfDays.days))
			return 0
			
		#Add days
		date = self.start + timedelta(days=int(day))

		if "hours" in attraction:
			
			if attraction["hours"] != None:
				if "week_ranges" in attraction["hours"]:
					
					if len(attraction["hours"]["week_ranges"]) >= int((self.start + timedelta(days=int(day)-1)).weekday()):
						
						if "times" in attraction["hours"]["week_ranges"][int((self.start + timedelta(days=int(day)-1)).weekday())+1]:
							
							if attraction["hours"]["week_ranges"][int((self.start + timedelta(days=int(day)-1)).weekday())+1]["times"] == []:
								print("Sorry but that attraction is closed on {}s".format(calendar.day_name[(self.start + timedelta(days=int(day)-1)).weekday()]))
								return 0
						
		self.attraction_choice[int(day)].append(attraction)
		
		
	def print_itinerary(self):
		for i in range(1, self.numberOfDays.days+1):
			print("Day {} {} {}".format(i, calendar.day_name[(self.start + timedelta(days=i-1)).weekday()], self.start + timedelta(days=i-1) ))
			print("\t Restaurants to visit:")
			for j in range(0, len(self.restaurant_choice[i])):
				print("\t\t {}. {}".format(j+1, self.restaurant_choice[i][j]["name"]))
				print("\t\t\t {}".format(self.restaurant_choice[i][j]["address_obj"]["address_string"]))
			print("\t Attractions to visit:")
			for j in range(0, len(self.attraction_choice[i])):
				print("\t\t {}. {}".format(j+1, self.attraction_choice[i][j]["name"]))
				print("\t\t\t {}".format(self.attraction_choice[i][j]["address_obj"]["address_string"]))
				
				
				