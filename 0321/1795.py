'''
인수의 생일 파티 D6

인수가 사는 마을에는 N개의 집이 있고, 각 집에는 한 명의 사람이 살고 있다.
N개의 집을 정점으로 볼 때, 도로는 어떤 집에서 다른 어떤 집으로 이동이 가능한 단방향 간선으로 볼 수 있으며, 각각에 대해서 이동하는데 시간이 정해져 있다.
도로는 모든 집들 간에 이동이 가능하도록 구성되어 있다.
집에 1번에서 N번까지의 번호를 붙일 때, 인수의 집은 X번 집이다.
오늘은 인수의 생일이기 때문에 모든 마을 사람들이 인수의 생일을 축하해주기 위해 X번 집으로 모인다.
각 사람들은 자신의 집에서 X번 집으로 오고 가기 위해 최단 시간으로 이동한다.
도로가 단 방향이기 때문에 이용하는 도로는 오고 갈 때 다를 것이다.

예를 들면 위와 같은 마을에서 X가 1인 경우
2번 집에서 1번 집으로 올 때 10, 갈 때 2의 걸려서 총 12이 걸리고,
3번 집에서도 총 12, 4번집에서도 총 12의 시간이 걸리고,
5번 집에서는 올 때 13, 갈 때 10의 시간이 걸려서 총 23의 시간이 걸리고,
5번 집이 1번 집으로 오고 가는데 가장 오랜 시간인 23의 시간이 걸린다.
X번 집으로 오고 가는데 드는 시간 중에서 가장 오래 걸리는 집은 어느 정도 걸리는지 구하는 프로그램을 작성하라.

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 세 정수 N,M,X(1 ≤ X ≤ N ≤ 1,000, 1 ≤ M ≤ 10,000)가 공백으로 구분되어 주어진다.
다음 M개의 각 줄에는 세 정수 x, y, c (1 ≤ x, y ＜ N, 1 ≤ c ≤ 100)가 공백으로 구분되어 주어진다.
이는 x번 집에서 y번 집으로 가는 데 시간이 c가 걸리는 단 방향 도로가 존재한다는 뜻이다.

[출력]
각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
오고 가는데 걸리는 시간이 가장 긴 거리를 출력한다.

[예제 풀이]
입력으로 주어진 데이터를 단방향 그래프로 나타내면 다음과 같이 그려진다.
여기서 각 노드에서 모이는 노드인 2번 노드로 오고 가는 최단 시간을 계산하고,
각 노드들의 최단 시간 중에서 가장 오래 걸리는 노드의 시간을 출력하는 문제이다.
우선 1번 노드는 2번노드로 갈 때 4(1→2), 올 때 1(2→1)의 시간이 걸리며, 오고 가는데 걸리는 시간은 5이다.
2번 노드는 목적지이므로 따로 계산할 필요가 없이 0이다.
3번 노드는 갈 때 6(3→1→2), 올 때 3(2→1→3)의 시간이 걸리고, 오고 가는데 걸리는 시간은 9이다.
4번 노드는 갈 때 3(4→2), 올 때 7(2→1→3→4)의 시간이 걸리고, 오고 가는데 걸리는 시간은 10이다.
따라서 입력 예제에서 4번 노드가 오고 가는데 가장 오랜 시간이 걸리며, 그 값은 10이다.
'''
# 입력 - 너무 길어서 간단한거만!
'''
1
4 8 2
1 2 4
1 3 2
1 4 7
2 1 1
2 3 5
3 1 2
3 4 4
4 2 3
'''
# 출력
'''
#1 10

#1 10
#2 213
#3 99
#4 253
#5 330
#6 294
#7 305
#8 346
#9 210
#10 50534

'''

import sys
sys.stdin = open('.txt', 'r')

import heapq

def dijkstra(start_node, arr):
    distance = [inf] * (N+1)
    distance[start_node] = 0
 
    pq = [[0, start_node]]

    while pq:
        dist, now_node = heapq.heappop(pq)

        for next_info in arr[now_node]:
            next_dist = next_info[0]
            next_node = next_info[1]

            new_dist = dist + next_dist

            if new_dist >= distance[next_node]:
                continue

            distance[next_node] = new_dist
            heapq.heappush(pq, [new_dist, next_node])

    return distance


T = int(input())
inf = int(21e9)

for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    rev_adj = [[] for _ in range(N+1)]
    
    distance = [inf] * (N+1)
    
    for _ in range(M):
        x, y, c = map(int, input().split())
        adj[x].append([c, y])
        rev_adj[y].append([c, x])

    max_time = 0

    go = dijkstra(X, rev_adj)
    back = dijkstra(X, adj)

    for i in range(1, N+1):
        now_time = go[i] + back[i]
        max_time = max(max_time, now_time)

    print(f'#{tc} {max_time}')