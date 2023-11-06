# AC, Показать сообщение:
# Группа Предварительные тесты
# Тест 1: OK
# Группа Основные тесты
# Итого за группу 100

n, k = map(int, input().split())

students = dict()

for _ in range(n):
    surname, icq = input().split()
    icq = int(icq)
    students[icq] = surname

sorted_icq = sorted(students.keys())
students = {icq: students[icq] for icq in sorted_icq[:k]}
print(*sorted(students.values()), sep='\n')
