# 아래 함수를 수정하시오.
# 홀수를 모두 제거하고 짝수만 남기기
# extend와 pop이용
def even_elements(lst):
    even_list = []
    i = 0
    while i < len(lst):
        number = lst[i]
        if number % 2 == 1:
            lst.pop(i)
        else:
            even_list.extend([number])
            i += 1
    return even_list


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
