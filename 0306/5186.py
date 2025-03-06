'''
 5186. [파이썬 S/W 문제해결 구현] 1일차 - 이진수2 D2

0보다 크고 1미만인 십진수 N을 이진수로 바꾸려고 한다. 예를 들어 0.625를 이진 수로 바꾸면 0.101이 된다.
N = 0.625
0.101 (이진수)
= 1*2-1 + 0*2-2 + 1*2-3
= 0.5 + 0 + 0.125
= 0.625
N을 소수점 아래 12자리 이내인 이진수로 표시할 수 있으면 0.을 제외한 나머지 숫자를 출력하고, 13자리 이상이 필요한 경우에는 ‘overflow’를 출력하는 프로그램을 작성하시오.

[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 소수점 아래가 12자리 이내인 N이 주어진다.

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
# 입력
'''
3
0.625
0.1
0.125
'''
# 출력
'''
#1 101
#2 overflow
#3 001
'''

# import sys
# sys.stdin = open("input.txt", "r")

def min_binary(num):
    global result
    cnt = 0
    a = -1
    while num>0:
        if num // (2**a):
            num -= 2**a
            result += '1'
            a -= 1
            
        else:
            result += '0'
            a -= 1

        cnt += 1
        if cnt > 12:
            result = 'overflow'
            break


T = int(input())

for tc in range(1,T+1):
    result = ''
    N = float(input())
    min_binary(N)

    print(f'#{tc} {result}')
