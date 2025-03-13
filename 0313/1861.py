'''
정사각형 방 D4

N2개의 방이 N×N형태로 늘어서 있다.
위에서 i번째 줄의 왼쪽에서 j번째 방에는 1이상 N2 이하의 수 Ai,j가 적혀 있으며, 이 숫자는 모든 방에 대해 서로 다르다.
당신이 어떤 방에 있다면, 상하좌우에 있는 다른 방으로 이동할 수 있다.
물론 이동하려는 방이 존재해야 하고, 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야 한다.
처음 어떤 수가 적힌 방에서 있어야 가장 많은 개수의 방을 이동할 수 있는지 구하는 프로그램을 작성하라.

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N (1 ≤ N ≤ 103)이 주어진다.
다음 N개의 줄에는 i번째 줄에는 N개의 정수 Ai, 1, … , Ai, N (1 ≤ Ai, j ≤ N2) 이 공백 하나로 구분되어 주어진다.
Ai, j는 모두 서로 다른 수이다.

[출력]
각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
한 칸을 띄운 후, 처음에 출발해야 하는 방 번호와 최대 몇 개의 방을 이동할 수 있는지를 공백으로 구분하여 출력한다.
이동할 수 있는 방의 개수가 최대인 방이 여럿이라면 그 중에서 적힌 수가 가장 작은 것을 출력한다.

[예제 풀이]
첫 번째 테스트 케이스는 1 또는 3이 적힌 곳에 있어야 한다.
두 번째 테스트 케이스는 3 또는 6이 적힌 곳에 있어야 한다.
'''
# 입력
'''
2
2
1 2
3 4
3
9 3 4
6 1 5
7 8 2
'''
# 출력
'''
#1 1 2
#2 3 3

#1 6 8
#2 3 2
#3 149 2
#4 2 45
#5 2 23
#6 1 2
#7 1 4
#8 5 17
#9 4 2
#10 1 35
#11 2 2
#12 7 2
#13 45 2
#14 113 2
#15 12 32
#16 6 9
#17 1 4
#18 36 42
#19 204 2
#20 7 14
#21 4 2
#22 8225 2200
#23 35 3
#24 2 2
#25 613 2
#26 33 2
#27 5 5


'''

import sys
sys.stdin = open('.txt', 'r')
# sys.stdout = open('result.txt', 'w')


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(r, c):
    visited = [[0]*N for _ in range(N)]
    visited[r][c] = 1
    q = [[r, c]]

    value = 0

    while q:
        tr, tc = q.pop(0)
        for d in range(4):
            nr = tr + dr[d]
            nc = tc + dc[d]

            if (
                0 <= nr < N
                and 0 <= nc < N
                and arr[nr][nc] == arr[tr][tc] + 1
                and not visited[nr][nc]
            ):
                visited[nr][nc] = visited[tr][tc] + 1
                if value < visited[nr][nc]:
                    value = visited[nr][nc]
                q.append([nr, nc])

    # print(visited, value)
    return value

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    ans1 = 1000000
    for r in range(N):
        for c in range(N):
            value = bfs(r, c)
            if value and result < value:
                result = value
                ans1 = arr[r][c]
                ans2 = value
            elif result == value and ans1 > arr[r][c]:
                ans1 = arr[r][c]

    print(f'#{tc} {ans1} {ans2}')

