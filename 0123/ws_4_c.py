matrix = [
        ['0, 1', '0, 2', '0, 3'], 
        ['1, 0', '1, 1', '1, 2', '1, 3'], 
        ['2, 0', '2, 1', '2, 2', '2, 3', '2, 4'], 
        ['3, 0', '3, 1'], 
        ['4, 0', '4, 1', '4, 2'], 
        ['5, 0']
    ]
# 아래애 코드를 작성하시오.

# matrix_len

matrix_len = 0
for i in matrix:
    matrix_len += 1

print(matrix_len)

# matrix 각 요소 길이

temporary_len = 0
for number in matrix:
    for i in number:
        temporary_len += 1
    if temporary_len <= 4:
        print(f'{number} 리스트는 {temporary_len}개 만큼 요소를 가지고 있습니다.')
    temporary_len = 0

# 인덱스 기준 순회

for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        print(f'matrix의 {x},{y} 번째 요소의 값은 {matrix[x][y]}입니다.')