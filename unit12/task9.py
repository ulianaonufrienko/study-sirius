n, m = list(map(int, input().split()))
a = []
b = []
c = []
for i in range(0,n):
    a.append(list(map(int, input().split())))
x = int(input())
for i in range(0,x):
    b.append(list(map(int, input().split())))
for i in range(0, len(b)):
    c.append(a[b[i][0]-1][b[i][1]-1])
    a[b[i][0] - 1][b[i][1] - 1] = 0
print(sum(c))
