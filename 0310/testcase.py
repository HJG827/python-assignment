import random

W = 4
H = 4

arr = [[0] * W for _ in range(H)]

for c in range(W):
    h = random.randint(0, H)
    for r in range(H-1, h, -1):
        arr[r][c] = random.randint(1, 9)

N = random.randint(1, 4)

print(1)
print(f"{N} {W} {H}")
for row in arr:
    print(' '.join([str(n) for n in row]))