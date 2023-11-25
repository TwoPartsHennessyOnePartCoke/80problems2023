# AC, Принята

n = int(input())

cars = {}
bt = 0

for i in range(n):
    c_num = int(input())
    t_diff = int(input())

    if cars.get(c_num) is None:
        cars[c_num] = t_diff + bt
    else:
        t = min(cars[c_num], t_diff + bt)
        cars.pop(c_num)
        cars[c_num] = t

    if t_diff < 0:
        bt += t_diff


sorted_cars = (sorted(cars.items(), key=lambda x: x[1]))
for i in sorted_cars:
    print(i[0], end=' ')
