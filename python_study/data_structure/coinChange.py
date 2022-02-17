def dp_coinChange(x):
    m = [2,5,7]
    f = [None] * 30
    f[0] = 0
    for i in range(1, x+1):
        f[i] = 1e9
        for j in range(len(m)):
            if i >= m[j]:
                f[i]=min(f[i-m[j]]+1, f[i])
    print(f[x])

dp_coinChange(27)
