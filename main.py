import datetime as DT

print(f"Today is - {DT.date.today()} and the time now is {DT.datetime.now().strftime("%H:%M:%S")}")
print(f"today is the {DT.date.weekday(DT.datetime.today())+1} day out of 7 in the week")