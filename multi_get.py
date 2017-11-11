import requests

def multi_get(ids):
    id_form = ",".join(ids)
    request_url = "http://api.tripadvisor.com/api//partner/2.0/location/{}/hotels?key=33b67ced-8002-4c51-a43b-ab2faa5e843e".format(id_form)
    response = requests.get(request_url)
    return response

if __name__ == "__main__":
    ids = ["89575","233835","192416"]
    data = multi_get(ids)

    print(data.text)
