import datetime
today = datetime.datetime.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days = 1)
print(yesterday.strftime('%A') , today.strftime('%A') , tomorrow.strftime('%A'))