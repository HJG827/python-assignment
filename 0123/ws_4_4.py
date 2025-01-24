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
            

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

censored_user_list = {}

def create_user():
    for user in dummy_data:
        result = censorship(user)        
        if result is True:
            censored_user_list[user['company']]=[user['name']]
        
        else:
            pass

    print(censored_user_list)

def censorship(user):
    if user['company'] in black_list:
        print(f'{user["company"]} 소속의 {user["name"]} 은/는 등록할 수 없습니다.')
        return False
    else:
        print('이상 없습니다.')
        return True
        

create_user()