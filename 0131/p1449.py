# 아래 함수를 수정하시오.
def intersection_sets(set1, set2):
    intersection = set()

    for item1 in set1:
        for item2 in set2:
            if item1 == item2:
                intersection.add(item1)
    if len(intersection):
        return (len(intersection), intersection)
    else: 
        print('공통 요소가 없습니다')
        return (len(intersection), intersection)


result = intersection_sets({1, 2, 3}, {3, 4, 5})
print(result)  # (1, {3})

result = intersection_sets({1, 2}, {3, 4})
print(result)  # (0, set())
# 출력: 공통 요소가 없습니다
