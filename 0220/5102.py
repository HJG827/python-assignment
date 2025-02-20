"""
 5102. [파이썬 S/W 문제해결 기본] 6일차 - 노드의 거리 D2

V개의 노드 개수와 방향성이 없는 E개의 간선 정보가 주어진다.
주어진 출발 노드에서 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는지 알아내는 프로그램을 만드시오.
예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경우, 두 개의 간선을 지나면 되므로 2를 출력한다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5<=V=50, 4<=E<=1000
테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 간선의 양쪽 노드 번호가 주어진다.
E개의 줄 이후에는 출발 노드 S와 도착 노드 G가 주어진다.

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
두 노드 S와 G가 서로 연결되어 있지 않다면, 0을 출력한다.
 
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6 
7 4
1 6
2 3
2 6
3 5
1 5 
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9

#1 2
#2 4
#3 3

"""


def bfs(s, g, V):
    visited = [0] * (V + 1)
    que = []
    que.append(s)
    visited[s] = 1

    while que:
        t = que.pop(0)

        if t == g:
            return visited[t] - 1

        for w in adj[t]:
            if not visited[w]:
                que.append(w)
                visited[w] = visited[t] + 1

    return 0


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V + 1)]
    for _ in range(E):
        n1, n2 = map(int, input().split())
        adj[n1].append(n2)
        adj[n2].append(n1)
    S, G = map(int, input().split())
    print(f"#{tc} {bfs(S, G, V)}")
