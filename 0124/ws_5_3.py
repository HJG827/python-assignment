# 아래 함수를 수정하시오.
def sort_tuple(tup):
    new_tuple = ()
    tup_lst = list(tup)
    result = sorted(tup_lst)
    new_tuple = tuple(result)

    return new_tuple


result = sort_tuple((5, 2, 8, 1, 3))
print(result)
