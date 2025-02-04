def ordered_difference_sets(set1, set2):
    result_set = set()
    if len(set2)>=len(set1):
        difference1 = set1-set2
        difference2 = set2-set1
    else:
        difference1 = set2-set1
        difference2 = set1-set2
    result_set = (difference1, difference2)
    return result_set

# 예시 실행
result = ordered_difference_sets({1, 2, 3, 4}, {3, 4, 5, 6})
print("결과:", result)  # 출력: ({1, 2}, {5, 6})

result = ordered_difference_sets({1, 2, 3, 4}, {1, 2, 3})
print("결과:", result)  # 출력: (set(), {4})
