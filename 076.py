# Use requests module to fetch API data

import requests

url = "https://api.github.com/users/octocat"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data["login"])
else:
    print("Error:", response.status_code)