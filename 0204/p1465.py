# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0
    def __init__(self, sound):
        self.sound = sound
        Animal.num_of_animal += 1

class Dog(Animal):
    sound = '멍멍' 
    def __init__(self, sound):
        super().__init__(sound)
    
    def bark(self):
        print('멍멍!')

class Cat(Animal):
    sound = '야옹' 
    def __init__(self, sound):
        super().__init__(sound)

    def meow(self):
        print('야옹!')

    

class Pet(Dog, Cat):

    def play(self):
        print('애완동물과 놀기')

    def make_sound(self):
        print(self.sound)

    @staticmethod
    def access_num_of_animal():
        return f'동물의 수는 {Animal.num_of_animal}마리 입니다.'
    
    def __str__(self):
        return f'애완동물은 {super().sound} 소리를 냅니다.'

    
    


pet1 = Pet("그르르")
print(pet1)