a = list(input().split())
m = 1000
for i in range(len(a)):
     s = int(a[i])
     if s < m and s > 0:
          m = s
print(m)
