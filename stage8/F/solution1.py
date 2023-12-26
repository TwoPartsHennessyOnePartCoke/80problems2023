# WA, Тест 4: неверный ответ

s, n = map(int, input().split())
cal = [0 for i in range(367)]
dates = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]

for i in range(n):
    day, month, payment = map(int, input().split())
    cal[day + dates[month - 1]] += payment

money = 0
bill = 0
m_bill = 0
for i in range(367):
    bill += m_bill
    if cal[i] != 0:
        money += cal[i]

    if (i in dates) and (i != 0):
        if money - s >= 0:
            money -= s
        elif money > 0:
            m_bill += (s / 1000) * (s - money)
            money = 0
        else:
            m_bill += (s / 1000)
    else:
        if money != 0 and m_bill != 0:
            d = min(m_bill, (money / s))
            m_bill -= d
            money -= d * s

print(f"{bill:.3f}")