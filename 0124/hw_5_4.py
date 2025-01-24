# 아래 함수를 수정하시오.
# 리스트의 최솟값과 최댓값 찾기
# 튜플로 반환하기기
def find_min_max(lst):
    lst.sort()
    min = lst[0]
    max = lst[len(lst)-1]

    return tuple([min, max])


result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
