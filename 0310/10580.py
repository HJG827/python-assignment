'''
10580. 전봇대 D3

현우는 길을 가다가 전선들이 복잡하게 꼬여 있는 전봇대 두 개를 보았다. 두 전봇대는 높이가 매우 높으며, N개의 팽팽한 전선으로 연결되어 있었다. 두 전선이 끝점이 같은 경우는 없으나, 교차하는 경우는 있다. 이를 그림으로 하면 아래와 같다. (전선 3개가 있으며, 교차점 2개가 검은색으로 칠해졌다.)

세 개 이상의 전선이 하나의 점에서 만나지 않는다고 가정하자. 이 전봇대에는 총 몇 개의 교차점이 있을까?

[입력]
첫 번째 줄에 테스트 케이스의 수 TC가 주어진다. 이후 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다. 각 테스트 케이스는 다음과 같이 구성되었다.
첫 번째 줄에 주어지는 전선의 개수 N이 주어진다 (1 ≤ N ≤1000).
이후 N개의 줄에 두 양의 정수 Ai, Bi 가 주어진다. (1 ≤ Ai, Bi ≤ 10000)이는 i번째 전선이, 첫번째 전봇대의 Ai cm 고도에 걸려 있고, 두 번째 전봇대의 Bi cm 고도에 걸려 있음을 뜻한다.
모든 Ai는 서로 다르고, 모든 Bi 도 서로 다르다. (두 전선의 끝점이 같은 경우가 없기 때문이다.) 세 전선이 한 점에서 만나지 않게 입력이 주어진다.


[출력]
각 테스트 케이스마다 한 줄씩 교차점의 개수를 출력하라.


'''
# 입력
'''
2
3
1 10
5 5
7 7
2
1 1
2 2
'''
# 출력
'''
#1 2
#2 0
'''

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    wires = []

    cross = 0

    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(len(wires)):
            if A < wires[i][0] and B > wires[i][1]:
                cross += 1
            if A > wires[i][0] and B < wires[i][1]:
                cross += 1

        wires.append([A, B])

    print(f'#{tc} {cross}')





