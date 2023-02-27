a = int(input())
b = int(input())
u = a // b
c = (u - 1) // (u + 1) + 1;
print(c * a + (1 - c) * b)
