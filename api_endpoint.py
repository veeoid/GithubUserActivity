import requests

API_URL = "https://api.github.com/users/"

def getUserData(username):
    request_url = API_URL + str(username) + '/events'
    response = requests.get(request_url)

    return response.json()

