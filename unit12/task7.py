n, m = map(int, input().split())

a = [[1]*m]*n

for i in range(m):
    print(a[0][i], end=' ')
print()

for i in range(n-1):
    i += 1
    print(a[0][0], end=' ')
    for j in range(m-1):
        j += 1
        a[i][j] = a[i][j-1] + a[i-1][j]
        print(a[i][j], end=' ')
    print()
