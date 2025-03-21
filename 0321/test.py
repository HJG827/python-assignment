
import sys
sys.stdin = open('.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    road = [1]

    for _ in range(M):
        x, y, c = map(int, input().split())
        adj[x].append([y, c])

    print(adj)
   
    