import requests
from geopy.geocoders import Nominatim

def multi_get(ids):
    id_form = ",".join(ids)
    request_url = "http://api.tripadvisor.com/api//partner/2.0/location/{}/hotels?key=33b67ced-8002-4c51-a43b-ab2faa5e843e".format(id_form)
    response = requests.get(request_url)
    return response

def address_get(address):

    location = geolocator.geocode(address)
    latitude = location.latitude
    longitude = location.longitude
    request_url = "http://api.tripadvisor.com/api/partner/2.0/map/{},{}?limit=3&offset=3%22&key=33b67ced-8002-4c51-a43b-ab2faa5e843e".format(latitude, longitude)
    response = requests.get(request_url)
    return response

if __name__ == "__main__":

    address = input("Enter an address you'd like to visit: ")
    geolocator = Nominatim()

    #location = geolocator.geocode(address)
    #print((location.latitude, location.longitude))

    x = address_get(address)
    print(x.text)
