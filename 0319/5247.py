'''
 5247. [파이썬 S/W 문제해결 구현] 6일차 - 연산 D3

자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만들려고 한다.
사용할 수 있는 연산이 +1, -1, *2, -10 네 가지라고 할 때 최소 몇 번의 연산을 거쳐야 하는지 알아내는 프로그램을 만드시오.
단, 연산의 중간 결과도 항상 백만 이하의 자연수여야 한다.
예를 들어 N=2, M=7인 경우, (2+1) *2 +1 = 7이므로 최소 3번의 연산이 필요한다.

[입력]
첫 줄에 테스트 케이스의 개수가 주어지고, 다음 줄부터 테스트 케이스 별로 첫 줄에 N과 M이 주어진다. 1<=N, M<=1,000,000, N!=M

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

'''
# 입력
'''
3
2 7
3 15
36 1007
'''
# 출력
'''
3
2 7
3 15
36 1007
'''

import sys
sys.stdin = open('.txt', 'r')

from collections import deque

def bfs(num):
    cnt = 0
    visited = set()
    q = deque([num])
    visited.add(num)

    while q:
        level_size = len(q)  # 현재 레벨에 있는 노드 수를 기록
        for _ in range(level_size):
            now_num = q.popleft()
            if now_num == M:
                return cnt
            for i in range(4):
                if i == 0:
                    next_num = now_num + 1
                if i == 1:
                    next_num = now_num - 1
                if i == 2:
                    next_num = now_num * 2
                if i == 3:
                    next_num = now_num - 10

                
                if next_num <= 1000000 and next_num not in visited:
                    visited.add(next_num)
                    q.append(next_num)
        cnt += 1
    return cnt
    

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    cal_lst = ['+1', '-1', '*2', '-10']

    print(f'#{tc} {bfs(N)}')