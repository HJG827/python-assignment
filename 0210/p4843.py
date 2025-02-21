"""
 4843. [파이썬 S/W 문제해결 기본] 2일차 - 특별한 정렬 D3
 
 보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.
N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.
예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.
10 1 9 2 8 3 7 4 6 5
주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄에 정수의 개수 N이 주어지고 다음 줄에 N개의 정수 ai가 주어진다. 10<=N<=100, 1<=ai<=100

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 특별히 정렬된 숫자를 10개까지 출력한다.

입력
3
10
1 2 3 4 5 6 7 8 9 10
10
67 39 16 49 60 28 8 85 89 11
20
3 69 21 46 43 60 62 97 64 30 17 88 18 98 71 75 59 36 9 26

출력
#1 10 1 9 2 8 3 7 4 6 5
#2 89 8 85 11 67 16 60 28 49 39
#3 98 3 97 9 88 17 75 18 71 21
"""

T = int(input())

for case_num in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N - 1):
        min_value = i
        for j in range(i + 1, N):
            if arr[min_value] > arr[j]:
                min_value = j
        arr[i], arr[min_value] = arr[min_value], arr[i]

    result = []

    min_idx = 0
    max_idx = N - 1

    while min_idx <= max_idx and len(result) < 10:
        if max_idx >= min_idx:
            result.append(arr[max_idx])
            max_idx -= 1

            result.append(arr[min_idx])
            min_idx += 1

    print(f"#{case_num} {' '.join(map(str, result))}")
