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
    global result
    share = num // 2
    remain = num % 2
    if share == 1:
        result += str(remain)
        result += '1'
    else:
        result += str(remain)
        dec_to_bin(share)

    return result[::-1]


number = int(input())
result = ''
print(dec_to_bin(number))
