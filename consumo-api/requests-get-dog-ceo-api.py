import requests

def dogceo_fetch():
    url_dogceo = "https://dog.ceo/api/breeds/list/all"
    response = requests.get(url_dogceo)
    response_json = response.json()
    for raza in response_json['message']:
        print(raza)
    return

dogceo_fetch()