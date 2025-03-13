'''
격자판의 숫자 이어 붙이기 D4

4×4 크기의 격자판이 있다. 격자판의 각 격자칸에는 0부터 9 사이의 숫자가 적혀 있다.
격자판의 임의의 위치에서 시작해서, 동서남북 네 방향으로 인접한 격자로 총 여섯 번 이동하면서, 각 칸에 적혀있는 숫자를 차례대로 이어 붙이면 7자리의 수가 된다.
이동을 할 때에는 한 번 거쳤던 격자칸을 다시 거쳐도 되며, 0으로 시작하는 0102001과 같은 수를 만들 수도 있다.
단, 격자판을 벗어나는 이동은 가능하지 않다고 가정한다.
격자판이 주어졌을 때, 만들 수 있는 서로 다른 일곱 자리 수들의 개수를 구하는 프로그램을 작성하시오.

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스마다 4개의 줄에 걸쳐서, 각 줄마다 4개의 정수로 격자판의 정보가 주어진다.

[출력]
각 테스트 케이스마다 ‘#x ’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 격자판을 이동하며 만들 수 있는 서로 다른 일곱 자리 수들의 개수를 출력한다.
 
'''
# 입력
'''
1
1 1 1 1
1 1 1 2
1 1 2 1
1 1 1 1

'''
# 출력
'''
#1 23

'''

import sys
sys.stdin = open('.txt', 'r')

def dfs(r, c, number):
    if len(number) == 7:
        if number not in numbers:
            numbers.add(number)
        return

    for dr, dc in ([0, 1], [1, 0], [0, -1], [-1, 0]):
        nr = r + dr
        nc = c + dc
        if (
            0 <= nr < 4
            and 0 <= nc < 4
        ):
            dfs(nr, nc, number+arr[nr][nc])


T= int(input())

for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]

    numbers = set()
    place = [[] for _ in range(10)]

    for r in range(4):
        for c in range(4):
            dfs(r, c, arr[r][c])


    print(f'#{tc} {len(numbers)}')

