
from datetime import date, datetime

today = date.today()
print("Today's date:", today)
today2 = datetime.now()
dt_string = today2.strftime("%Y-%m-%d.%H-%M-%S")
print(dt_string)