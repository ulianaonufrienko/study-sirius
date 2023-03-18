S = input()
Letters = dict()
for i in S:
    if i.isalpha():
        if i.upper() in Letters:
            Letters[i.upper()] += 1
        else:
            Letters[i.upper()] = 1
max = 0
for key in Letters:
    if Letters[key] > max:
        max = Letters[key]
answer = "";
for code in range(ord('A'), ord('Z') + 1):
    character = chr(code)
    if character in Letters and Letters[character] == max:
        answer += character

print(answer)
print(max)
