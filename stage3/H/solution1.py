# AC, Принята

from datetime import datetime
def h24(time):
    time_ = datetime.strptime(time, "%I:%M%p")
    return time_.hour * 60 + time_.minute

def h12(minutes):
    time_obj = datetime(2023, 1, 1, minutes // 60, minutes % 60)
    return time_obj.strftime("%I:%M%p")

N = int(input())
calls = []
for _ in range(N):
    start_time, end_time = input().split()
    start_minutes = h24(start_time)
    end_minutes = h24(end_time)
    time=[start_minutes, end_minutes]
    calls.append(time)

slots=[]
for i in range(0,54):
    if 24>i or i>29:
        slots.append(8*60+10*i)

for call in calls:
    s_time,e_time=call
    r_time="N/A"

    for slot_s in slots:
        if slot_s>=s_time and slot_s <=e_time:
            r_time=h12(slot_s)
            slots.remove(slot_s)
            break
    r_time=str(r_time)
    if "PM" in r_time:
        r_time=r_time.replace("PM","pm")
    if "AM" in r_time:
        r_time=r_time.replace("AM","am")
    if r_time[0]=="0":
        r_time=r_time[1:]
    print(r_time)
