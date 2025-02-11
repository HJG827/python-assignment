dy = [0, 0, -1]  # 왼 오 위
dx = [-1, 1, 0]


def ladder():
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    y = 99
    x = arr[99].index(2)

    while y > 0:
        for i in range(2):
            new_y = y + dy[i]
            new_x = x + dx[i]
            # 양옆 확인
            if 0 <= new_x < 100 and arr[new_y][new_x] == 1:
                while 0 <= new_x < 100 and arr[new_y][new_x] == 1:
                    x, y = new_x, new_y
                    new_x += dx[i]
                break
        y += dy[2]

    return x


for tc in range(1, 11):
    print(f"#{tc} {ladder()}")
