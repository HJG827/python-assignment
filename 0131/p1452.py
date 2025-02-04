# 아래 함수를 수정하시오.
def remove_duplicates_to_set(lst):
    unique_lst = []
    for number in lst:
        if number not in unique_lst:
            unique_lst.append(number)

    return set(unique_lst)

result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)
