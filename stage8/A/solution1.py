# AC, Принята

s = str(input())

words = []
for i in range(len(s)):
    s_n = s
    s_n = s_n[:i] + s_n[i + 1:]
    words.append(s_n)

print(sorted(words)[0])