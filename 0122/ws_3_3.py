def rental_book(name, number):
    global number_of_book
    decrease_book(number)
    print(f'남은 책의 수 : {number_of_book}')
    print(f'{name}님이 {number}권의 책을 대여하였습니다.')
    pass

number_of_book = 100

def decrease_book(number):
    global number_of_book
    number_of_book -= number
    pass


rental_book('홍길동', 3)