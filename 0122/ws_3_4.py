# number_of_people = 0


# def increase_user():
#     pass


# def create_user(name, age, address):
#     for one_name in name:
#         print(f'{one_name}님 환영합니다!')
#     user_info = [{
#         'name': name,
#         'age': age,
#         'address': address
#     } for name, age, address in user_list]
#     print(user_info)
   
#     pass


# name = ['김시습', '허균', '남영로', '임제', '박지원']
# age = [20, 16, 52, 36, 60]
# address = ['서울', '강릉', '조선', '나주', '한성부']

# user_list = list(zip(name, age, address))

# create_user(name, age, address)


number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1



def create_user(name, age, address):
    for one_name in name:
        print(f'{one_name}님 환영합니다!')
    
    def to_dict(tuple):
        name, age, address = tuple
        return {
        'name': name,
        'age': age,
        'address': address
    }
    
    user_info = {
        'name': name,
        'age': age,
        'address': address
    }

    user_list= list(map(to_dict, list(zip(name, age, address))))
    # user_list = list(map(create_user, name, age, address))
    print(user_list)

    pass


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']



create_user(name, age, address)
