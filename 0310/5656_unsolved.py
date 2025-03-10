'''
5656. [모의 SW 역량테스트] 벽돌 깨기

구술을 쏘아 벽돌을 깨트리는 게임을 하려고 한다.
구슬은 N번만 쏠 수 있고, 벽돌들의 정보는 아래와 같이 W x H 배열로 주어진다.
( 0 은 빈 공간을 의미하며, 그 외의 숫자는 벽돌을 의미한다. )

게임의 규칙은 다음과 같다.
① 구슬은 좌, 우로만 움직일 수 있어서 항상 맨 위에 있는 벽돌만 깨트릴 수 있다.
② 벽돌은 숫자 1 ~ 9 로 표현되며,
   구술이 명중한 벽돌은 상하좌우로 ( 벽돌에 적힌 숫자 - 1 ) 칸 만큼 같이 제거된다.
아래는 벽돌에 적힌 숫자와, 구술이 명중했을 시 제거되는 범위의 예이다.
③ 제거되는 범위 내에 있는 벽돌은 동시에 제거된다.
예를 들어 아래와 같이 4 번 벽돌에 구술이 명중할 경우,
9번 벽돌은 4 번 벽돌에 반응하여,
동시에 제거된다.
④ 빈 공간이 있을 경우 벽돌은 밑으로 떨어지게 된다.

N 개의 벽돌을 떨어트려 최대한 많은 벽돌을 제거하려고 한다.
N, W, H, 그리고 벽돌들의 정보가 주어질 때,
▶ 남은 벽돌의 개수를 구하라!

※ sample input 1

N = 3, W = 10, K = 10 이고 벽돌들의 정보가 아래와 같을 때,

최대한 많은 벽돌을 깨트리는 방법은 아래와 같으며, 정답은 12 가 된다.
그림의 빨간 색 원은 구술이 명중한 위치이며, 주황색 칸은 폭발의 범위를 의미한다.

i) 첫 번째 구술
ii) 두 번째 구술
iii) 세 번째 구술

[제약 사항]
1. 1 ≤ N ≤ 4
2. 2 ≤ W ≤ 12
3. 2 ≤ H ≤ 15

[입력]
가장 첫 줄에는 총 테스트 케이스의 개수 T 가 주어지고,
그 다음 줄부터 T 개의 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 N, W, H 가 순서대로 공백을 사이에 두고 주어지고,
다음 H 줄에 걸쳐 벽돌들의 정보가 1 줄에 W 개씩 주어진다.

[출력]
출력은 #t 를 찍고 한 칸 띄운 다음 정답을 출력한다.
(t 는 테스트 케이스의 번호를 의미하며 1 부터 시작한다)
'''
# 입력
'''
5
3 10 10
0 0 0 0 0 0 0 0 0 0
1 0 1 0 1 0 0 0 0 0
1 0 3 0 1 1 0 0 0 1
1 1 1 0 1 2 0 0 0 9
1 1 4 0 1 1 0 0 1 1
1 1 4 1 1 1 2 1 1 1
1 1 5 1 1 1 1 2 1 1
1 1 6 1 1 1 1 1 2 1
1 1 1 1 1 1 1 1 1 5
1 1 7 1 1 1 1 1 1 1
2 9 10
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0 0
1 1 0 0 1 0 0 0 0
1 1 0 1 1 1 0 1 0
1 1 0 1 1 1 0 1 0
1 1 1 1 1 1 1 1 0
1 1 3 1 6 1 1 1 1
1 1 1 1 1 1 1 1 1
3 6 7
1 1 0 0 0 0
1 1 0 0 1 0
1 1 0 0 4 0
4 1 0 0 1 0
1 5 1 0 1 6
1 2 8 1 1 6
1 1 1 9 2 1
4 4 15
0 0 0 0 
0 0 0 0 
0 0 0 0 
1 0 0 0 
1 0 0 0 
1 0 0 0 
1 0 0 0 
1 0 5 0 
1 1 1 0 
1 1 1 9 
1 1 1 1 
1 6 1 2 
1 1 1 5 
1 1 1 1 
2 1 1 2 
4 12 15
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
'''
# 출력
'''
#1 12
#2 27
#3 4
#4 8
#5 0
'''

from collections import deque
# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('result.txt', 'w')

from copy import deepcopy

def perm(idx):
    global min_blocks

    if idx == N:
        if min_blocks == 0:
            return
        
        copy_blocks = deepcopy(blocks)
        for i in range(N):
            col = ball[i]
            row = -1

            for r in range(H):
                if copy_blocks[r][col]:
                    row = r
                    break
            if row == -1:
                continue

            copy_blocks = bfs(row, col, copy_blocks)
   
        min_blocks = min(min_blocks, check_blocks(copy_blocks))
        return
    
    for w in range(W):
        ball[idx] = w
        perm(idx+1)


# 벽돌 하나를 터뜨릴 때 한번에 터지는 것을 표현
def bfs(r, c, arr):
    visited = [[0]*W for _ in range(H)]

    q  = deque()
    q.append([r, c, arr[r][c]])
    
    visited[r][c] = 1
    while q:
        tr, tc, power = q.popleft()
        if arr[tr][tc]:
            for dr, dc in ([0, 1], [1, 0], [0, -1], [-1, 0]):
                for d in range(1, power):
                    nr = tr + dr*d
                    nc = tc + dc*d
                    if (
                        0 <= nr < H
                        and 0 <= nc < W
                        and arr[nr][nc]
                        and not visited[nr][nc]
                    ):
                        visited[nr][nc] = visited[tr][tc] + 1
                        if arr[nr][nc] > 1:
                            q.append([nr, nc, arr[nr][nc]])

    # 폭발!
    for r in range(H):
        for c in range(W):
            if visited[r][c]:
                arr[r][c] = 0

    # 벽돌 중력 적용
    return organize_blocks(arr)            


# 박스 중력으로 내리기
def organize_blocks(arr):
    for c in range(W):
        for r in range(H-1, -1, -1):
            if arr[r][c] == 0:
                for i in range(r-1, -1, -1):
                    if arr[i][c]:
                        arr[r][c], arr[i][c] = arr[i][c], arr[r][c]
                        break
    
    return arr

# 남은 벽돌 확인
def check_blocks(arr):
    block = 0
    for r in range(H):
        for c in range(W):
            if arr[r][c]:
                block += 1
    
    return block

T = int(input())

for tc in range(1, T+1):
    N, W, H = map(int, input().split())

    blocks = [list(map(int, input().split())) for _ in range(H)]

    min_blocks = W*H

    ball = [0]*N
    perm(0)
    
    print(f'#{tc} {min_blocks}')







