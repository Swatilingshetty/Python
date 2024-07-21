# a =[12,32,65,121,43,232,45]

# list1=[]
# def check(a):
#     for ele in a:
#         list1.append(ele+5)
#     return list1
# print(check(a))

import csv
# with open ('team info.csv','r') as file:
#     read_data=csv.reader(file)
#     for row in read_data:
#         if row[1]=="CSK":
#          print(row)


# with open('records.csv') as file:
#    read_data=csv.reader(file)
#    for row in read_data:
#       if row[4]=='bheem@123gmail.com':
#          print(row)

def record(firtsname,lastname):
    firtsname=firtsname
    lastname=lastname
    return firtsname,lastname

names=map(record('firtsname'),('lastname'))
print(record)
