"""
[S/W 문제해결 기본] 3일차 - 회문1 D3

8x8 평면 글자판에서 제시된 길이를 가진 회문의 개수를 구하라.
위와 같은 글자판이 주어졌을 때, 길이가 5인 회문은 붉은색 테두리로 표시된 4개이므로 4를 반환하면 된다.

[제약 사항]
각 칸의 들어가는 글자는 'A', 'B', 'C' 중 하나이다.
ABA도 회문이며, ABBA도 회문이다. A 또한 길이 1짜리 회문이다.
가로 또는 세로로 이어진 회문의 개수만 센다.
아래 그림에서 노란색 경로를 따라가면 길이 7짜리 회문이 되지만 직선이 아니기 때문에 인정되지 않는다.

[입력]
총 10개의 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 찾아야 하는 회문의 길이가 주어지며, 다음 줄에 8x8 크기의 글자판이 주어진다.

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 찾은 회문의 개수를 출력한다.
"""

for tc in range(1, 11):
    N = int(input())

    arr = [list(input()) for _ in range(8)]
    result = 0

    for r in range(8):
        for c in range(8 - N + 1):
            txt = arr[r][c : c + N]
            if txt == txt[::-1]:
                result += 1

    for c in range(8):
        for r in range(8 - N + 1):
            txt = "".join(arr[r + i][c] for i in range(N))
            if txt == txt[::-1]:
                result += 1

    print(f"#{tc} {result}")
