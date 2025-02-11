"""
[S/W 문제해결 기본] 5일차 - GNS D3

숫자 체계가 우리와 다른 어느 행성이 있다. 아래는 이 행성에서 사용하는 0 ~ 9의 값을 순서대로 나타낸 것이다.
"ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"
0 ~ 9 의 값을 나타내는 단어가 섞여 있는 문자열을 받아 작은 수부터 차례로 정렬하여 출력하는 프로그램을 작성하라.
예를 들어 입력 문자열이 "TWO NIN TWO TWO FIV FOR" 일 경우 정렬한 문자열은 "TWO TWO TWO FOR FIV NIN" 이 된다.

[입력]
입력 파일의 첫 번째 줄에는 테스트 케이스의 개수가 주어진다.
그 다음 줄에 #기호와 함께 테스트 케이스의 번호가 주어지고 공백 문자 후 테스트 케이스의 길이가 주어진다.
테스트 케이스의 길이란, 문자열의 글자수가 아닌 단어의 갯수를 말한다.
그 다음 줄부터 바로 테스트 케이스가 주어진다. 단어와 단어 사이는 하나의 공백으로 구분하며, 문자열의 길이 N은 100≤N≤10000이다.

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 정렬된 문자열을 출력한다.

"""


def Alien_Number_sort(A, N, arr):

    alien_numbers = [
        "ZRO",
        "ONE",
        "TWO",
        "THR",
        "FOR",
        "FIV",
        "SIX",
        "SVN",
        "EGT",
        "NIN",
    ]

    alien_dict = {}
    result = []

    for alien_num in alien_numbers:
        alien_dict[alien_num] = 0
        for i in range(len(arr)):
            if arr[i] == alien_num:
                if arr[i] in alien_dict:
                    alien_dict[alien_num] += 1
                else:
                    alien_dict[alien_num] = 1

    for a in range(10):
        if not (alien_dict[alien_numbers[a]] == 0 or alien_numbers[a] is False):

            for _ in range(alien_dict[alien_numbers[a]]):
                result.append(alien_numbers[a])
    print(f"#{tc}")
    print("".join(result))


T = int(input())

for tc in range(1, T + 1):
    A, N = input().split()
    arr = list(input().split())
    Alien_Number_sort(A, N, arr)
