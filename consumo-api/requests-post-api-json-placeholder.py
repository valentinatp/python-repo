import requests

def jsonplaceholder_fetch():
    url_jsonplaceholder_api = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url_jsonplaceholder_api)
    response_json = response.json()
    print(response)
    print(response_json)
    return

def jsonplaceholder_post():
    url_jsonplaceholder_api = "https://jsonplaceholder.typicode.com/"

    pass

jsonplaceholder_fetch()
jsonplaceholder_post()