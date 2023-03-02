n = int(input())
m=n%100
if m <= 10 or m >= 20:
    if (m % 10) == 0 or ((m % 10) >= 5 and (m % 10) <= 9):
        print(str(n) + " bochek")
    elif (m % 10) == 1:
        print(str(n) + " bochka")
    else:
        print(str(n) + " bochki")
else:
    print(str(n) + " bochek")
