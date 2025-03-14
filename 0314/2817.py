'''
부분 수열의 합 D3

A1, A2, ... , AN의 N개의 자연수가 주어졌을 때, 최소 1개 이상의 수를 선택하여 그 합이 K가 되는 경우의 수를 구하는 프로그램을 작성하시오.

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 2개의 자연수 N(1 ≤ N ≤ 20)과 K(1 ≤ K ≤ 1000)가 주어진다.
두 번째 줄에는 N개의 자연수 수열 A가 주어진다. 수열의 원소인 N개의 자연수는 공백을 사이에 두고 주어지며, 1 이상 100 이하임이 보장된다.

[출력]
각 테스트 케이스마다 ‘#x ’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 부분 수열의 합이 K가 되는 경우의 수를 출력한다.
'''
# 입력
'''
1
4 3
1 2 1 2
'''
# 출력
'''
#1 4
'''

import sys
sys.stdin = open('.txt', 'r')

def find(arr):
    subsets = []

    for i in range(1<<N):
        subset = []
        for j in range(N):
            if i & (1<<j):
                subset.append(arr[j])

        if sum(subset) == K:
            subsets.append(subset)

    return len(subsets)


T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    print(f'#{tc} {find(A)}')
    

