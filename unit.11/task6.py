a = list(map(int, input().split()))
count = 0
k = []
for x in a:
     if x not in k:
          count += 1
          k.append(x)
print(len(k))

