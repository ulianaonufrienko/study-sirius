def CaesarCipherChar(c, k):
    if 'a' <= c <= 'z':
        a= chr((ord(c) - 97 + k) % 26 + 97)
    elif 'A' <= c <= 'Z':
        a= chr((ord(c) - 65 + k) % 26 + 65)
    else:
        a = c
    return a

def CaesarCipher(s,k):
    S=''
    for i in s:
        S+=CaesarCipherChar(i,k)
    return S


x = CaesarCipher("iHknmzfkdkfdkmfk", 3)
print(x)
