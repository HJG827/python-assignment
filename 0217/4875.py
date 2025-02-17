"""
 4875. [파이썬 S/W 문제해결 기본] 5일차 - 미로 D2

NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성하시오. 도착할 수 있으면 1, 아니면 0을 출력한다.
주어진 미로 밖으로는 나갈 수 없다.

다음은 5x5 미로의 예이다.

13101
10101
10101
10101
10021

마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 도착할 수 있는지 확인하면 된다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 0은 통로, 1은 벽, 2는 출발, 3은 도착이다. 5<=N<=100

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.

입력
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000

출력
#1 1
#2 1
#3 0
"""


def dfs(r, c):
    if arr[r][c] == 3:
        return 1

    visited[r][c] = 1

    # 상하좌우 설정
    dir_r = [0, 1, 0, -1]
    dir_c = [1, 0, -1, 0]

    for i in range(4):
        next_r = r + dir_r[i]
        next_c = c + dir_c[i]

        if (
            0 <= next_r < N
            and 0 <= next_c < N
            and arr[next_r][next_c] != 1
            and not visited[next_r][next_c]
        ):
            if dfs(next_r, next_c):
                return 1

    return 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                start_r = r
                start_c = c
    print(f"#{tc} {dfs(start_r, start_c)}")
