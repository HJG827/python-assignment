"""
 4881. [파이썬 S/W 문제해결 기본] 5일차 - 배열 최소 합 D2

NxN 배열에 숫자가 들어있다. 한 줄에서 하나씩 N개의 숫자를 골라 합이 최소가 되도록 하려고 한다. 단, 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.
조건에 맞게 숫자를 골랐을 때의 최소 합을 출력하는 프로그램을 만드시오.
예를 들어 다음과 같이 배열이 주어진다.
 
212
585
722

이경우 1, 5, 2를 고르면 합이 8로 최소가 된다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 첫 줄에 숫자 N이 주어지고, 이후 N개씩 N줄에 걸쳐 10보다 작은 자연수가 주어진다. 3≤N≤10

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 합계를 출력한다.

3
3
2 1 2
5 8 5
7 2 2
3
9 4 7
8 6 5
5 3 7
5
5 2 1 1 9
3 3 8 3 1
9 2 8 8 6
1 5 7 8 3
5 5 4 6 8

#1 8
#2 14
#3 9

"""


def minimum_sum(a, N, s):
    global min_sum

    if a == N:
        if min_sum > s:
            min_sum = s

    elif min_sum < s:
        return

    else:
        for i in range(a, N):
            p[a], p[i] = p[i], p[a]
            minimum_sum(a + 1, N, s + arr[a][p[a]])
            p[a], p[i] = p[i], p[a]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    p = list(range(N))
    min_sum = 10000
    minimum_sum(0, N, 0)
    print(f"#{tc} {min_sum}")
