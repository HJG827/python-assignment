# 아래 함수를 수정하시오.
def reverse_string(text):
    result = reversed(text)
    return ''.join(result)
    


result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH
