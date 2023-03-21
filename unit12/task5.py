n = int(input())
A = [0]*n
for i in range(n):
    A[i] = list(map(int, input().split()))
for i in range(n):
    A[i][i], A[n-1-i][i] = A[n-1-i][i], A[i][i]
for i in range(n):
    for j in range(n):
        print(A[i][j],end=' ')
    print()
