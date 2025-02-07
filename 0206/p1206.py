# [S/W 문제해결 기본] 1일차 - View
# 왼쪽과 오른쪽으로 창문을 열었을 때, 양쪽 모두 거리 2 이상의 공간이 확보될 때 조망권이 확보된다고 말한다.
# 빌딩들에 대한 정보가 주어질 때, 조망권이 확보된 세대의 수를 반환하는 프로그램을 작성하시오.
# 아래와 같이 강변에 8채의 빌딩이 있을 때, 연두색으로 색칠된 여섯 세대에서는 좌우로 2칸 이상의 공백이 존재하므로 조망권이 확보된다. 따라서 답은 6이 된다.

# [제약 사항]
# 가로 길이는 항상 1000이하로 주어진다.
# 맨 왼쪽 두 칸과 맨 오른쪽 두 칸에는 건물이 지어지지 않는다. (예시에서 빨간색 땅 부분)
# 각 빌딩의 높이는 최대 255이다.
 
# [입력]
# 총 10개의 테스트케이스가 주어진다.
# 각 테스트케이스의 첫 번째 줄에는 건물의 개수 N이 주어진다. (4 ≤ N ≤ 1000)
# 그 다음 줄에는 N개의 건물의 높이가 주어진다. (0 ≤ 각 건물의 높이 ≤ 255)
# 맨 왼쪽 두 칸과 맨 오른쪽 두 칸에 있는 건물은 항상 높이가 0이다. (예시에서 빨간색 땅 부분)
 
# [출력]
# #부호와 함께 테스트케이스의 번호를 출력하고, 공백 문자 후 조망권이 확보된 세대의 수를 출력한다...

# 입력
# 10
# 0 0 254 185 76 227 84 175 0 0
# 10
# 0 0 251 199 176 27 184 75 0 0
# 11
# 0 0 118 90 243 178 99 100 200 0 0
# ...

# 출력
# #1 111
# #2 60
# #3 165
# ...

for case_num in range(10):
    N = int(input())
    building = list(map(int,input().split()))
    count = 0
    for i in range(1, N-1):
        if max(building[i-2],building[i-1]) < building[i] and building[i] > max(building[i+1], building[i+2]):
            left_height = building[i] - max(building[i-2],building[i-1])
            right_height = building[i] - max(building[i+1], building[i+2])
            building_view = min(left_height, right_height)
            count += building_view
    print(f'#{case_num+1} {count}')
