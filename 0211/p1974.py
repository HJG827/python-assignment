"""
스도쿠 검증 D2

같은 줄에 1 에서 9 까지의 숫자를 한번씩만 넣고, 3 x 3 크기의 작은 격자 또한, 1 에서 9 까지의 숫자가 겹치지 않아야 한다.
입력으로 9 X 9 크기의 스도쿠 퍼즐의 숫자들이 주어졌을 때, 위와 같이 겹치는 숫자가 없을 경우, 1을 정답으로 출력하고 그렇지 않을 경우 0 을 출력한다.

[제약 사항]
1. 퍼즐은 모두 숫자로 채워진 상태로 주어진다.
2. 입력으로 주어지는 퍼즐의 모든 숫자는 1 이상 9 이하의 정수이다.

[입력]
입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
다음 줄부터 각 테스트 케이스가 주어진다.
테스트 케이스는 9 x 9 크기의 퍼즐의 데이터이다.

[출력]
테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
"""

T = int(input())

for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    result = 1
    nine = [range(1, 10)]

    for r in range(9):
        row_check = set()
        col_check = set()

        for c in range(9):
            if arr[r][c] in row_check:
                result = 0
                break
            row_check.add(arr[r][c])

            if arr[c][r] in col_check:
                result = 0
                break
            col_check.add(arr[c][r])
        if result == 0:
            break

    for r_start in range(0, 9, 3):
        for c_start in range(0, 9, 3):
            box_check = set()

            for r in range(3):
                for c in range(3):
                    number = arr[r_start + r][c_start + c]
                    if number in box_check:
                        result = 0
                        break
                box_check.add(number)

    print(f"#{tc} {result}")
