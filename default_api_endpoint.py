import json
import urllib.request as request

API_URL = "https://api.github.com/users/"

def get_userdata(username):
    request_url = API_URL + username + "/events"

    try:
        with request.urlopen(request_url) as response:
            if response.status != 200:
                raise Exception(f"Error fetching data: {response.status}")
            data = json.loads(response.read().decode())

    except Exception as e:
        print(f"An error occurred: {e}")
        data = []
    return data