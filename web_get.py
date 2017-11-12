import requests
from geopy.geocoders import Nominatim
import json

def web_get_hotel(address):
    geolocator = Nominatim()
    location = geolocator.geocode(address)
    latitude = location.latitude
    longitude = location.longitude

    request_url = "http://api.tripadvisor.com/api/partner/2.0/map/{},{}/hotels?limit=10&offset=0%22&key=33b67ced-8002-4c51-a43b-ab2faa5e843e".format(latitude, longitude)
    response = requests.get(request_url)

    data = json.loads(response.text)
    return data

def web_get_restaurant(address):
    geolocator = Nominatim()
    location = geolocator.geocode(address)
    latitude = location.latitude
    longitude = location.longitude

    request_url = "http://api.tripadvisor.com/api/partner/2.0/map/{},{}/restaurants?limit=20&offset=0%22&key=33b67ced-8002-4c51-a43b-ab2faa5e843e".format(latitude, longitude)
    response = requests.get(request_url)

    data = json.loads(response.text)
    return data

def web_get_attraction(address):
    geolocator = Nominatim()
    location = geolocator.geocode(address)
    latitude = location.latitude
    longitude = location.longitude

    request_url = "http://api.tripadvisor.com/api/partner/2.0/map/{},{}/attractions?limit=20&offset=0%22&key=33b67ced-8002-4c51-a43b-ab2faa5e843e".format(latitude, longitude)
    response = requests.get(request_url)

    data = json.loads(response.text)
    return data

if __name__ == "__main__":
    geolocator = Nominatim()

    #location = geolocator.geocode(address)
    #print((location.latitude, location.longitude))

    x = web_get(address)


    data = json.loads('{}'.format(x.text))
   # pprint(data)

    city = data["data"][0]["address_obj"]["city"]
    country = data["data"][0]["address_obj"]["country"]
