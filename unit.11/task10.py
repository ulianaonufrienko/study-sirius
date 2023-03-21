a = list(map(int, input().split()))
idx_min = a.index(min(a))
idx_max = a.index(max(a))
a[idx_min], a[idx_max] = a[idx_max], a[idx_min]
print(' '.join(map(str, a)))
