import requests
import json
from pprint import pprint

username = 'dotnet'

url = f"https://api.github.com/users/{username}"

user_data = requests.get(url).json()

filtered_data = {key: user_data[key] for key in ['company', 'created_at', 'email', 'id', 'name', 'url']}

pprint(filtered_data)

with open('filtered_data.json', 'w') as file:
    json.dump(filtered_data, file, indent=4)