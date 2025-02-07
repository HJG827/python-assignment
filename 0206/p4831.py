#  4831. [파이썬 S/W 문제해결 기본] 1일차 - 전기버스 D3
# A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.
# 버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.
# 충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.
# 만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.
 
#  [입력]
# 첫 줄에 노선 수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다. ( 1 ≤ K, N, M ≤ 100 )
 
# [출력]
# #과 노선번호, 빈칸에 이어 최소 충전횟수 또는 0을 출력한다.

# 입력
# 3
# 3 10 5
# 1 3 5 7 9
# 3 10 5
# 1 3 7 8 9
# 5 20 5
# 4 7 9 14 17

# 출력
# #1 3
# #2 0
# #3 4

T = int(input())

for case_num in range(1, T+1):
    K, N, M = map(int,input().split())
    charge_spot = list(map(int,input().split()))

    # charge = [0]*(N+1)
    # count_charge = 0
    
    # for i in range(M):
    #     charge[charge_spot[i]] += 1
    
    # idx = 0
    # while idx < N:
    #     if charge[K] == 1:
    #         idx += K
    #         count_charge += 1
        
    #     else:
    #         for i in range(K-1, -1, -1):
    #             if charge[i] == 1:
    #                 idx += i
    #                 count_charge += 1

    now = 0
    count_charge = 0

    while now + K < N:
        next_position = now # 현재 위치 업데이트 및 충전소 못 찾은 경우 대비용!!!!!!!
        for distance in range(K, 0, -1):
            if (now + distance) in charge_spot:
                next_position = now + distance
                break

        if next_position == now:
            count_charge = 0
            break

        now = next_position
        count_charge += 1

    print(f'#{case_num} {count_charge}')





    