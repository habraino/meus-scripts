import datetime as dt

day_delta = dt.timedelta(days=1)
start_day = dt.date.today()
end_day = start_day + 7 * day_delta

for i in range((end_day - start_day).days):
    day = start_day + i * day_delta
    print(day)

print('*'*20)
for j in range((end_day - start_day).days):
    may = end_day + j * day_delta
    print(may)
