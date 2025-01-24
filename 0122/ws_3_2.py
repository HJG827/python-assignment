number_of_people = 0
print(f'현재 가입 된 유저 수 : {number_of_people}')


def increase_user():
    global number_of_people
    number_of_people += 1
    pass
# pass는 함수에 본문이 없을 때 에러가 나지 말라고 넣어두는 것
# 본문이 있으면 지우면 됨!

def create_user(name, age, address):
    print(f'{name}님 환영합니다!')
    user_info = {
        'name': name,
        'age': age,
        'address': address
    }
    print(user_info)
    increase_user()
    print(f'현재 가입 된 유저 수 : {number_of_people}')
    pass

create_user('홍길동', 30, '서울')
