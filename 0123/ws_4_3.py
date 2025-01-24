import requests
from pprint import pprint as print

dummy_data = []

for i in range(1, 11):
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
    response = requests.get(API_URL)
    parsed_data = response.json()
    dict = {
        'company': parsed_data['company']['name'],
        'lat': parsed_data['address']['geo']['lat'],
        'lng': parsed_data['address']['geo']['lng'],
        'name': parsed_data['name']
    }
    if float(dict['lat']) < 80:
        if float(dict['lng']) > -80:
            dummy_data.append(dict)
            
        
print(dummy_data)