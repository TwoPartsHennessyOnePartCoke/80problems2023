# AC, Принята

n = int(input())
for _ in range(n):
    hours, minutes = map(int, input().split(':'))
    total_minutes = hours * 60 + minutes

    while True:
        total_minutes = (total_minutes + 1) % (24 * 60)
        hours, minutes = divmod(total_minutes, 60)

        if str(hours).zfill(2) == str(minutes).zfill(2)[::-1]:
            print(str(hours).zfill(2) + ':' + str(minutes).zfill(2))
            break
