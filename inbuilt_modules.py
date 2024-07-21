# inbuilt modules: those modules which are already built in python..

# print(help('modules'))

# import symtable

# print(help('symtable'))

# random,  datetime,json,CSV, OS, tkinter

# import random

# print(dir(random))

# print(random.random(1,1000))

# print(random.randint(100000,999999))

# print(random.choice(["SWIGGYY11","SWIGGYY20","SWIGGYY30","SWIGGYY40","SWIGGYY50"]))

# print(id(random.choice))

#datetime module..

# import datetime

# print(dir(datetime.time))

from datetime import datetime , timedelta
# print(dir(datetime))

# print(datetime.now())

# print(datetime.now().date())

# print(datetime.now().time())

# print(type(datetime.now()))

# print(type(datetime.now().date()))

# print(type(datetime.now().time()))

# now_date=datetime.now()

# print(now_date)

# after_30=now_date+timedelta(days=30)

# print(after_30)

# after_30=now_date+timedelta(months=3)  #error-it wont with months..

# print(after_30)

# from dateutil.relativedelta import relativedelta

# after_3months = now_date + relativedelta(months=3)

# print(after_3months)

# march_2=now_date=timedelta(days=12)

# # print(march_2)

# march_2+timedelta(days=90)

# print(march_2+relativedelta(months=3))

now_date=datetime.now()

# print(now_date)

# strftime: for converting date into string format..

# str_date=now_date.strftime('%d,%m,%y')

# print(str_date)
# print(type(str_date))



# str_date=now_date.strftime('%d-%m-%y')
#  print(str_date)
# print(type(str_date))

# str_date=now_date.strftime('%d/%m/%y')
# print(str_date)
# print(type(str_date))

# str_date=now_date.strftime('%d/%m/%y %h-%m-%s')
# print(str_date)
# print(type(str_date))

# now_date=now_date+timedelta(hours=5)

# str_date=now_date.strftime('%d,%m,%y %h,%m,%S')
# print(str_date)
# print(type(str_date))

# str_date=now_date.strftime('%d,%m,%y %h:%m:%S %p %a %A %b %B')
# print(str_date)
# print(type(str_date))

# strptime(): for converting string into python datetime format..

# str_date='24/05/1998 07:43 AM'
# print(str_date)
# print(type(str_date))

# py_datetime=datetime.strptime(str_date,'%d/%m/%Y %I:%M %p')

# print(py_datetime)

# print(type(py_datetime))

# urliltb:
