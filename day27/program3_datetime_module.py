import datetime

today = datetime.date.today()
current_time = datetime.datetime.now()

print("Today's Date:", today)
print("Current Time:", current_time.strftime("%H:%M:%S"))
print("Current Year:", today.year)
print("Current Month:", today.month)
print("Current Day:", today.day)