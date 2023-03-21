a = list(map(int, input().split()))
m = a[0]
count = a.count(m)
for elem in a:
     if a.count(elem) > count:
          m = elem
          count = a.count(elem)
print(m)
