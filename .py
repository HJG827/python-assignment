text = input()
number_lst = []

for char in text:
    number = ord(char)-64
    number_lst.append(number)
print(*number_lst)