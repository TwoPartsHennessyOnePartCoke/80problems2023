# AC, Показать сообщение
# Группа Основные тесты
# Итого за группу 100

text = input().strip().lower()
find = input().strip().lower()
text=text.replace(' ','')
find=find.replace(' ','')
letters={}
f=0

for i in text:
    if i in letters:
        letters[i] += 1
    else:
        letters[i] = 1

for i in find:
    if i in letters and letters[i]>0:
        letters[i]-=1
    else:
        f=1
        break
if f==0:
    print("YES")
else:
    print("NO")