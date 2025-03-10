
def bfs(r, c, arr):
    visited = [[0]*W for _ in range(H)]
    q = [[r, c, arr[r][c]]]
    
    visited[r][c] = 1
    while q:
        tr, tc, power = q.pop(0)
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



T = int(input())

for tc in range(1, T+1):
    N, W, H = map(int, input().split())

    blocks = [list(map(int, input().split())) for _ in range(H)]

    for row in blocks:
        print(row)
    min_blocks = W*H

    # ball = [0]*N
    # perm(0)
    
    result = bfs(8, 6, blocks)
    print('==============')
    for row in result:
        print(row)