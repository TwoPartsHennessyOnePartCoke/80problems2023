# AC, Принята

def find_months(day):
    months=[i for i in range(1,13)]
    day_in_months=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month=0

    while day>day_in_months[month]:
        day-=day_in_months[month]
        month+=1

    return day,months[month]
N = int(input())
day,month=find_months(N)
print(day,month)