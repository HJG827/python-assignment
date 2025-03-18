'''
5208. [파이썬 S/W 문제해결 구현] 5일차 - 전기버스2 D3
충전지를 교환하는 방식의 전기버스를 운행하려고 한다. 정류장에는 교체용 충전지가 있는 교환기가 있고, 충전지마다 최대로 운행할 수 있는 정류장 수가 정해져 있다.
충전지가 방전되기 전에 교체하며 운행해야 하는데 교체하는 시간을 줄이려면 최소한의 교체 횟수로 목적지에 도착해야 한다.
정류장과 충전지에 대한 정보가 주어질 때, 목적지에 도착하는데 필요한 최소한의 교환횟수를 출력하는 프로그램을 만드시오. 단, 출발지에서의 배터리 장착은 교환횟수에서 제외한다.
다음은 1번에서 출발 5번이 종점인 경우의 예이다.

정류장
1
2
3
4
5
충전지
2
3
1
1

1번에서 장착한 충전지 용량이 2이므로, 3번 정류장까지 운행할 수 있다. 그러나 2번에서 미리 교체하면 종점까지 갈 수 있다.
마지막 정류장에는 배터리가 없다.

[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 한 줄에 정류장 수 N, N-1개의 정류장 별 배터리 용량 Mi가 주어진다. 3<=N<=100, 0 ＜ Mi ＜ N

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다
'''

# 입력
'''
3
5 2 3 1 1
10 2 1 3 2 2 5 4 2 1
10 1 1 2 1 2 2 1 2 1
'''
# 출력
'''
#1 1
#2 2
#3 5
'''

import sys
sys.stdin = open('.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, *numbers = map(int, input().split())
    numbers = [0] + numbers

    idx = 1
    battery = numbers[idx]
    charge = 0

    while idx < N:
        max_range = 0
        next_station = idx
        for i in range(1, battery + 1):
            # 정류장 번호가 N을 넘지 않도록 검사
            
            if idx + i < N:
                # 도달 가능한 정류장: 현재 idx + i + numbers[idx + i]
                reach = idx + i + numbers[idx + i]
                if reach > max_range:
                    max_range = reach
                    next_station = idx + i
                    # print(f"현재 idx: {idx}, i: {i}, reach: {reach}, max_range: {max_range}, next_station: {next_station}")
        if max_range >= N:
            idx = N
            charge += 1
            break

        # 다음 배터리로 교환할 정류장을 선택
        battery = numbers[next_station]
        idx = next_station
        charge += 1


    print(f'#{tc} {charge}')

