'''
 5204. [파이썬 S/W 문제해결 구현] 4일차 - 병합 정렬 D3

알고리즘 교수님은 학생들에게 병합 정렬을 이용해 오름차순으로 정렬하는 과제를 내려고 한다.
정렬 된 결과만으로는 실제로 병합 정렬을 적용했는지 알 수 없기 때문에 다음과 같은 제약을 주었다.
N개의 정렬 대상을 가진 리스트 L을 분할할 때 L[0:N//2], L[N//2:N]으로 분할 한다.
병합 과정에서 다음처럼 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력한다.
정렬이 끝난 리스트 L에서 L[N//2] 원소를 출력한다.
알고리즘 교수님의 조건에 따라 병합 정렬을 수행하는 프로그램을 만드시오.

[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 정수의 개수 N이 주어지고, 다음 줄에 N개의 정수 ai가 주어진다.
5<=N<=1,000,000, 0 <= ai <= 1,000,000

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤,  N//2 번째 원소와 오른쪽 원소가 먼저 복사되는 경우의 수를 출력한다.


'''
# 입력
'''
2
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8
'''
# 출력
'''
#1 2 0
#2 6 6
'''

import sys
sys.stdin = open('.txt', 'r')

def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # 원소가 하나 이하라면 그대로 반환
    
    mid = len(arr) // 2  # 배열을 반으로 나눌 기준점
    left_half = merge_sort(arr[:mid])  # 왼쪽 부분 정렬
    right_half = merge_sort(arr[mid:])  # 오른쪽 부분 정렬
    
    return merge(left_half, right_half)  # 정렬된 두 부분을 합치기

def merge(left, right):
    global cnt
    result = []  # 정렬된 배열을 저장할 리스트
    i = j = 0  # 두 리스트의 인덱스


    if left[-1] > right[-1]:
        cnt += 1

    while i < len(left) and j < len(right):
        if left[i] < right[j]:  # 더 작은 값을 선택
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 남은 원소들을 추가
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    cnt = 0
    sorted_numbers = merge_sort(numbers)

    print(f'#{tc} {sorted_numbers[N//2]} {cnt}')
    

    