# AC, Принята

from collections import defaultdict
n = int(input())
l_to_e = defaultdict(list)

for i in range(n):
    line = input().split(' - ')
    e_word = line[0]
    l_t = line[1].split(', ')
    
    for l_word in l_t:
        l_to_e[l_word].append(e_word)

print(len(l_to_e))
for l_word, translations in sorted(l_to_e.items()):
    translations = sorted(translations)
    print(f"{l_word} - {', '.join(translations)}")