a = input().split()
ans = 0
for i in range(len(a)):
     for j in range(i + 1, len(a)):
          if a[i] == a[j]:
               ans += 1
print(ans)
