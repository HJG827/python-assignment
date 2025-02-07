arr = [3, 6, 7, 1, 5, 4]

n = len(arr)
subsets = []

for i in range(1<<n):
    subset = []
    for j in range(n):
        if i & (1<<j):
            subset.append(arr[j])
    subsets.append(subset)
    
    print(subset)