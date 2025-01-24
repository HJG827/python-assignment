# 아래 함수를 수정하시오.
def remove_duplicates(lst):
    new_lst = []
    for number in lst:
        if number not in new_lst:
            new_lst.append(number)
    return new_lst


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)
