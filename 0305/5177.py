'''
 5177. [파이썬 S/W 문제해결 기본] 8일차 - 이진 힙 D2


이진 최소힙은 다음과 같은 특징을 가진다.
    - 항상 완전 이진 트리를 유지하기 위해 마지막 노드 뒤에 새 노드를 추가한다.
    - 부모 노드의 값<자식 노드의 값을 유지한다. 새로 추가된 노드의 값이 조건에 맞지 않는 경우, 조건을 만족할 때까지 부모 노드와 값을 바꾼다.
    - 노드 번호는 루트가 1번, 왼쪽에서 오른쪽으로, 더 이상 오른쪽이 없는 경우 다음 줄로 1씩 증가한다.
예를 들어 7, 2, 5, 3, 4, 6이 차례로 입력되면 다음과 같은 트리가 구성된다.

이때 마지막 노드인 6번의 조상은 3번과 1번 노드이다.
1000000이하인 N개의 서로 다른 자연수가 주어지면 입력 순서대로 이진 최소힙에 저장하고, 마지막 노드의 조상 노드에 저장된 정수의 합을 알아내는 프로그램을 작성하시오.

[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 N이 주어지고, 다음 줄에 1000000이하인 서로 다른 N개의 자연수가 주어진다. 5<=N<=500

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

3
6
7 2 5 3 4 6
6
3 1 4 16 23 12
8
18 57 11 52 14 45 63 40

#1 7
#2 5
#3 65

'''
def heap(n):
    global last
    last += 1
    tree[last] = n
    c = last
    p = c//2
    while p and tree[p] > tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c//2

def sum_anc(n):
    idx = N
    result = 0
    while idx>0:
        idx //= 2
        result += tree[idx]
    
    return result

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    tree = [0] * (N+1)
    last = 0
    for i in range(N):
        heap(numbers[i])

    result = sum_anc(tree[N-1])
    print(f'#{tc} {result}')