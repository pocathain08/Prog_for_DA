#Program to check if it is tuesday. P O Cathain 20 Oct 2019

import datetime

today = datetime.datetime.today()
dayofweek = today.weekday()

if dayofweek == 1:
    print("It's Tuesday!")
else:
    print("Unofortunately, it's not Tuesday.")


