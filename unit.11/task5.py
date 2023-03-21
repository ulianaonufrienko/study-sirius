a = [int(i) for i in input().split()]
k, c = [int(i) for i in input().split()]
a.append(0)
for j in range(len(a) - 1, k, -1):
     a[j] = a[j - 1]
a[k] = c
print(' '.join([str(j) for j in a]))
