# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0
    def __init__(self, name):
        Animal.num_of_animal += 1


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def bark(self):
        print('멍멍!')

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def meow(self):
        print('야옹!')


class Pet(Dog, Cat):
    @staticmethod
    def access_num_of_animal():
        return f'동물의 수는 {Animal.num_of_animal}마리 입니다.'


cat1 = Cat("야옹")
cat1.meow()