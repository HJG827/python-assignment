'''
[도전] 10진수를 2진수로 변환하는 재귀 함수를 생성하라

10
8
42

1010
1000
101010
'''
def dec_to_bin(num):
    # 0 입력 시 '0' 반환
    if num == 0:
        return '0'  
     # 1이면 바로 '1' 반환 (기본 종료 조건)
    if num == 1:
        return '1' 

     # 재귀적으로 나머지를 이어붙임
    return dec_to_bin(num // 2) + str(num % 2) 

# 입력 및 출력
number = int(input())
print(dec_to_bin(number))
