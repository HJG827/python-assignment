# 달팽이 숫자
# 달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.
# 다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.

# 입력
# 2    
# 3   
# 4             
 
# 출력
# #1
# 1 2 3
# 8 9 4
# 7 6 5
# #2
# 1 2 3 4
# 12 13 14 5
# 11 16 15 6
# 10 9 8 7

T = int(input())
dir_r = [0, 1, 0, -1]
dir_c = [1, 0, -1, 0]
for case_num in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    r = c = 0
    direction = 0
    number = 1

    while number <= N**2:
        arr[r][c] = number
        number += 1

        next_r = r + dir_r[direction]
        next_c = c + dir_c[direction]

        if not (0<=next_r<N and 0<=next_c<N and arr[next_r][next_c] ==0):
            direction = (direction+1) % 4
            next_r = r + dir_r[direction]
            next_c = c + dir_c[direction]

        r, c = next_r, next_c

    print(f'#{case_num}')

    for snail in arr:
        print(' '.join(map(str, snail)))