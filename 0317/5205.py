'''
 5205. [파이썬 S/W 문제해결 구현] 4일차 - 퀵 정렬 D3

퀵 정렬을 구현해 N개의 정수를 정렬해 리스트 A에 넣고, A[N//2]에 저장된 값을 출력하는 프로그램을 만드시오.

[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 정수의 개수 N이 주어지고, 다음 줄에 N개의 정수 ai가 주어진다.
5<=N<=1,000,000, 0 <= ai <= 1,000,000

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, , N/2번 원소를 출력한다.

'''
# 입력
'''
2
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8
'''
#출력
'''
#1 2
#2 6
'''

import sys
sys.stdin = open('.txt', 'r')

def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i + 1

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    quick_sort(numbers, 0, len(numbers) - 1)

    print(f'#{tc} {numbers[N//2]}')
    