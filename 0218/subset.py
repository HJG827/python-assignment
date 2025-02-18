# 부분집합 재귀로 구현하기


def f(idx):
    if idx == N:  # 이미 완성되었으므로 더 이상 결정할 필요 X (N번 인덱스 X)
        print(out)
        return
    else:
        out[idx] = 1
        f(idx + 1)
        out[idx] = 0
        f(idx + 1)


arr = [1, 2, 3, 4, 5]
N = len(arr)
out = [False] * N

# idx번째 숫자를 포함할지 말지 여부(T/F)를 결정한 후
# 그 다음 수(idx+1) 결정하러 감
f(0)
