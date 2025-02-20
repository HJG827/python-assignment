"""
 5105. [파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리 D3

NxN 크기의 미로에서 출발지 목적지가 주어진다.
이때 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 알아내는 프로그램을 작성하시오.
경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수를, 경로가 없는 경우 0을 출력한다.
다음은 5x5 미로의 예이다. 1은 벽, 0은 통로를 나타내며 미로 밖으로 벗어나서는 안된다.

13101
10101
10101
10101
10021

마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 5개의 칸을 지나 도착할 수 있다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 5<=N<=100
0은 통로, 1은 벽, 2는 출발, 3은 도착이다.

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

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

#1 5
#2 5
#3 0

"""


def bfs(r, c):
    visited = [[0] * N for _ in range(N)]
    que = []
    que.append([r, c])
    visited[r][c] = 1

    while que:
        tr, tc = que.pop(0)
        if maze[tr][tc] == 3:
            return visited[tr][tc] - 2

        for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr = tr + dr
            nc = tc + dc
            if (
                0 <= nr < N
                and 0 <= nc < N
                and maze[nr][nc] != 1
                and not visited[nr][nc]
            ):
                que.append([nr, nc])
                visited[nr][nc] = visited[tr][tc] + 1

    return 0


def find_start(N):
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                return r, c


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    start_r, start_c = find_start(N)
    print(f"#{tc} {bfs(start_r, start_c)}")
