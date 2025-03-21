'''
[모의 SW 역량테스트] 등산로 조성

등산로를 조성하려고 한다.
등산로를 만들기 위한 부지는 N * N 크기를 가지고 있으며, 이곳에 최대한 긴 등산로를 만들 계획이다.
등산로 부지는 아래 [Fig. 1]과 같이 숫자가 표시된 지도로 주어지며, 각 숫자는 지형의 높이를 나타낸다.
 
등산로를 만드는 규칙은 다음과 같다.
   ① 등산로는 가장 높은 봉우리에서 시작해야 한다.
   ② 등산로는 산으로 올라갈 수 있도록 반드시 높은 지형에서 낮은 지형으로 가로 또는 세로 방향으로 연결이 되어야 한다.
       즉, 높이가 같은 곳 혹은 낮은 지형이나, 대각선 방향의 연결은 불가능하다.
   ③ 긴 등산로를 만들기 위해 딱 한 곳을 정해서 최대 K 깊이만큼 지형을 깎는 공사를 할 수 있다.
N * N 크기의 지도가 주어지고, 최대 공사 가능 깊이 K가 주어진다.
이때 만들 수 있는 가장 긴 등산로를 찾아 그 길이를 출력하는 프로그램을 작성하라.

[예시]
위 [Fig. 1]과 같이 N = 5인 지도가 주어진 경우를 살펴보자.
가장 높은 봉우리는 높이가 9로 표시된 세 군데이다.
이 세 곳에서 출발하는 가장 긴 등산로 중 하나는 아래 [Fig. 2]와 같고, 이 때 길이는 5가 된다.
만약 최대 공사 가능 깊이 K = 1로 주어질 경우,
아래 [Fig. 3]과 같이 빨간색 부분의 높이를 9에서 8로 깎으면 길이가 6인 등산로를 만들 수 있다.
이 예에서 만들 수 있는 가장 긴 등산로는 위와 같으며, 출력할 정답은 6이 된다.

[제약 사항]
1. 시간 제한 : 최대 51개 테스트 케이스를 모두 통과하는 데 C/C++/Java 모두 3초
2. 지도의 한 변의 길이 N은 3 이상 8 이하의 정수이다. (3 ≤ N ≤ 8)
3. 최대 공사 가능 깊이 K는 1 이상 5 이하의 정수이다. (1 ≤ K ≤ 5)
4. 지도에 나타나는 지형의 높이는 1 이상 20 이하의 정수이다.
5. 지도에서 가장 높은 봉우리는 최대 5개이다.
6. 지형은 정수 단위로만 깎을 수 있다.
7. 필요한 경우 지형을 깎아 높이를 1보다 작게 만드는 것도 가능하다.

[입력]
입력의 맨 첫 줄에는 총 테스트 케이스의 개수 T가 주어지고, 그 다음 줄부터 T개의 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 지도의 한 변의 길이 N, 최대 공사 가능 깊이 K가 차례로 주어진다.
그 다음 N개의 줄에는 N * N 크기의 지도 정보가 주어진다.

[출력]
테스트 케이스 개수만큼 T개의 줄에 각각의 테스트 케이스에 대한 답을 출력한다.
각 줄은 "#t"로 시작하고 공백을 하나 둔 다음 정답을 출력한다. (t는 1부터 시작하는 테스트 케이스의 번호이다)
출력해야 할 정답은 만들 수 있는 가장 긴 등산로의 길이이다.
'''
# 입력
'''
10
5 1
9 3 2 3 2
6 3 1 7 5
3 4 8 9 9
2 3 7 7 7
7 6 5 5 8
3 2
1 2 1
2 1 2
1 2 1
5 2
9 3 2 3 2
6 3 1 7 5
3 4 8 9 9
2 3 7 7 7
7 6 5 5 8
4 4
8 3 9 5
4 6 8 5
8 1 5 1
4 9 5 5
4 1
6 6 1 7
3 6 6 1
2 4 2 4
7 1 3 4
5 5
18 18 1 8 18
17 7 2 7 2
17 8 7 4 3
17 9 6 5 16
18 10 17 13 18
6 4
12 3 12 10 2 2
13 7 13 3 11 6
2 2 6 5 13 9
1 12 5 4 10 5
11 10 12 8 2 6
13 13 7 4 11 7
7 3
16 10 14 14 15 14 14
15 7 12 2 6 4 9
10 4 11 4 6 1 1
16 4 1 1 13 9 14
3 12 16 14 8 13 9
3 4 17 15 12 15 1
6 6 13 6 6 17 12
8 5
2 3 4 5 4 3 2 1
3 4 5 6 5 4 3 2
4 5 6 7 6 5 4 3
5 6 7 8 7 6 5 4
6 7 8 9 8 7 6 5
5 6 7 8 7 6 5 4
4 5 6 7 6 5 4 3
3 4 5 6 5 4 3 2
8 2
5 20 15 11 1 17 10 14
1 1 11 16 1 14 7 5
17 2 3 4 5 13 19 20
6 18 5 16 6 7 8 5
10 4 5 4 9 2 10 16
2 7 16 5 8 9 10 11
12 19 18 8 7 11 15 12
1 20 18 17 16 15 14 13

'''
# 출력
'''
#1 6
#2 3
#3 7
#4 4
#5 2
#6 12
#7 6
#8 7
#9 10
#10 19
'''

import sys
sys.stdin = open('.txt', 'r')

dr = [1, 0, -1, 0]
dc = [0, -1, 0, 1]

def find_high(arr):
    max_number = 0
    lst = []
    for r in range(N):
        for c in range(N):
            if max_number < arr[r][c]:
                lst = [[r, c]]
                max_number = arr[r][c]

            elif arr[r][c] == max_number:
                lst.append([r, c])
    return lst

def dfs(r, c, cnt, do):
    global visited, result

    result = max(cnt, result)

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if (
            0 <= nr < N
            and 0 <= nc < N
            and not visited[nr][nc]
        ):
            if arr[nr][nc] < arr[r][c]:
                visited[nr][nc] = 1
                dfs(nr, nc, cnt + 1, do)
                visited[nr][nc] = 0

            else:
                differ = arr[nr][nc] - arr[r][c] + 1
                if differ <= K and do:
                    visited[nr][nc] = 1
                    arr[nr][nc] -= differ
                    dfs(nr, nc, cnt + 1, do - 1)
                    arr[nr][nc] += differ
                    visited[nr][nc] = 0
    

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0]*N for _ in range(N)]
    start = find_high(arr)
    result = 0

    for r, c in start:
        visited[r][c] = 1
        dfs(r, c, 1, 1)
        visited[r][c] = 0

    print(f'#{tc} {result}')