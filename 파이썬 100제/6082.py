N = int(input())

for i in range(1, N+1):
    if (i//10==3) and (i%10==3 or i%10==6 or i%10==9):
        print("XX", end=' ')
    elif (i//10==3) and (i%10!=3 or i%10!=6 or i%10!=9):
        print("X", end=' ')
    elif (i//10!=3) and (i%10==3 or i%10==6 or i%10==9):
        print("X", end=' ')
    else:
        print(i, end=' ')

    