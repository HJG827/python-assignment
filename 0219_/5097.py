"""
 5097. [파이썬 S/W 문제해결 기본] 6일차 - 회전 D2

N개의 숫자로 이루어진 수열이 주어진다. 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 했을 때, 수열의 맨 앞에 있는 숫자를 출력하는 프로그램을 만드시오.
[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 첫 줄에 N과 M이 주어지고, 다음 줄에 10억 이하의 자연수 N개가 주어진다. 3<=N<=20, N<=M<=1000,

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 번호를 출력한다.

3
3 10
5527 731 31274 
5 12
18140 14618 18641 22536 23097 
10 23
17236 31594 29094 2412 4316 5044 28515 24737 11578 7907

#1 731
#2 18641
#3 2412
"""


def number_change(N, M):
    numbers = list(map(int, input().split()))
    que = numbers
    time = M % N
    for _ in range(time):
        t = que.pop(0)
        que.append(t)
    return que[0]


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    print(f"#{tc} {number_change(N,M)}")
