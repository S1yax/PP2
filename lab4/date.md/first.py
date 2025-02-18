import datetime
x = datetime.datetime.now()
five_days = datetime.timedelta(days=5)
answer = x - five_days
print(answer)