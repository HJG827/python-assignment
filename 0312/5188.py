'''
 5188. [파이썬 S/W 문제해결 구현] 2일차 - 최소합 D3

그림처럼 NxN 칸에 숫자가 적힌 판이 주어지고, 각 칸에서는 오른쪽이나 아래로만 이동할 수 있다.
맨 왼쪽 위에서 오른쪽 아래까지 이동할 때, 지나는 칸에 써진 숫자의 합계가 최소가 되도록 움직였다면 이때의 합계가 얼마인지 출력하는 프로그램을 만드시오.
그림의 경우 1, 2, 3, 4, 5순으로 움직이고 최소합계는 15가 된다. 가능한 모든 경로에 대해 합을 계산한 다음 최소값을 찾아도 된다.

[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 첫 줄에 가로 세로 칸 수 N이 주어지고, 다음 줄부터 N개씩 N개의 줄에 걸쳐 10이하의 자연수가 주어진다. 3<=N<=13
 
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
# 입력
'''
3
3
1 2 3
2 3 4
3 4 5
4
2 4 1 3
1 1 7 1
9 1 7 10
5 7 2 4
5
6 7 1 10 2
10 2 7 5 9
9 3 2 9 6
1 6 8 2 9
8 3 8 2 1

'''
# 출력
'''
#1 15
#2 18
#3 33
'''

import sys
sys.stdin = open('i.txt', 'r')

def find_way(r, c):
    global min_count, cnt, visited
    
    visited[r][c] = 1
    cnt += arr[r][c]

    if r == N-1 and c == N-1:
        min_count = min(cnt, min_count)

    else:
        for dr, dc in ([0, 1], [1, 0]):
            nr = r + dr
            nc = c + dc

            if (
                0 <= nr < N
                and 0 <= nc < N
                and not visited[nr][nc]
            ):
                if cnt + arr[nr][nc] < min_count:
                    find_way(nr, nc)
                
    
    visited[r][c] = 0
    cnt -= arr[r][c]
        

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0]*N for _ in range(N)]
    cnt = 0
    min_count = 50000
    find_way(0,0)

    print(f'#{tc} {min_count}')
