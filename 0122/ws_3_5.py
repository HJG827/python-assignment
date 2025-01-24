number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

def to_dict(tuple):
        name, age, address = tuple
        return {
        'name': name,
        'age': age,
        'address': address
    }


def create_user(name, age, address):
    for one_name in name:
        print(f'{one_name}님 환영합니다!')

    
    # user_info = {
    #     'name': name,
    #     'age': age,
    #     'address': address
    # }
    
    pass

many_user= list(map(to_dict, list(zip(name, age, address))))
# print(many_user)

# print(list(zip(name,age, address)))

# info= list(map(to_dict2, list(zip(name, age))))
info = list(map(lambda x: {'name': x[0], 'age': x[1]},zip(name, age)))
# print(info)


def rental_book(info):
    global number_of_book
    
    number = info['age']//10

    decrease_book(number)
    print(f'남은 책의 수 : {number_of_book}')
    print(f"{info['name']}님이 {number}권의 책을 대여하였습니다.")
    pass



number_of_book = 100

def decrease_book(number):
    global number_of_book
    number_of_book -= number
    pass



create_user(name, age, address)
list(map(rental_book, info))