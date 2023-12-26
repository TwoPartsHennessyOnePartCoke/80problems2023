# 83, Показать сообщение
# Группа Предварительные тесты
# Тест 1: OK
# Группа Основные тесты
# Тест 2: неверный ответ
# Тест 12: неверный ответ
# Итого за группу 83

x0, n = map(int, input().split())
y0 = 1e10
coord = []

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    coord.append([x1, y1, x2, y2])

while len(coord) != 0:
    yp = -1
    ip = -1
    for i in range(len(coord)):
        if (coord[i][0] < x0) and (coord[i][2] > x0):
            if max(coord[i][1], coord[i][3]) > yp:
                yp = max(coord[i][1], coord[i][3])
                ip = i

    x0 = coord[ip][0] if coord[ip][1] < coord[ip][3] else coord[ip][2]
    y0 = min(coord[ip][1], coord[ip][3])
    coord.pop(ip)

    coord_new = []
    for j in range(len(coord)):
        if min(coord[j][1], coord[j][3]) < y0:
            coord_new.append(coord[j])
    coord = [coord_new[k] for k in range(len(coord_new))]

print(x0)
