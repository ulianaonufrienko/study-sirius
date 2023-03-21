a = input().split()
a[1::2] = a[1::2][::-1]
print(' '.join(a))
