# file_operations: different operations which we can perform on files..

# on text files we can perform the operations directly itself ..

# opening the file..

# 1st way of opening the file..
#  file_obj= open ('file_name',"mode")

# 2nd way of opening the file 
    # with open('file_name','mode') as file :
   # pass

# swati=open('new_req.txt','r')   # r-read mode.

# print(swati)

# print(swati.closed)

# file_obj=open('new_req.txt','r')   # r-read mode.

# print(file_obj)

# print(file_obj.closed)

# with open('new_req.txt','r') as file:
#     print(file)

# print(file.closed)

# modes of opening the file..
#  r- Read mode
#  w- write mode
#  a-append mode 
    
# reading:
#   read 
#   readline
#   readlines

# with open('new_req.txt','r') as file:
#     print(file.read())  #its reading the data charecter by charector .
#     print(file.readline)
#     print(file.readlines)  # its redaing the data line by line.

# writing: it means overwriting the content of the file.
# write()- its for writing 1 string of content into the file at a time.
# writelines()-
    
# with open('write_text.txt','w') as file:

    # file.write('this is first write line statements\n')
    # file.write('this is second write line statements\n')

    # file.writelines(['this is first write line statements\n','this is second write line statements\n','this is third write line statements\n'])

#appending: it means adding the content  at the end of the file..
# write:
# writlines:

# with open('write_text.txt','a') as file:
    # file.write('this is fourth write line statment\n')

    # file.writelines(['this is second write line statement\n','this is third write line statement\n'])

# first.txt task..
  # a=13

# second.txt
  # b=32

# third.txt
  # c=a-b
  # c=-19


# file operations on csv File 
# csv- comma seperated values

# import csv

# with open('team info.csv','r') as file:
#     read_data=csv.reader(file)
# #     # print(read_data)
#     for row in read_data:
#         if row[2]=='batsman' and int(row[0]=='Rohith'):
#             print(row)

# for row in read_data:
#     print(row[0],row[1])

# for col in read_data:
#     print(col[0],col[1])

# writerow: its for writing 1 row of data at a time..
# writwrows: its for writing multiple rows of data at a time..

# with open("team_info_write.csv",'w',newline="") as file:
#     write_data=csv.writer(file)
#     write_data.writerow(['team name','captain','year of incaption'])
#     write_data.writerow(['MI','Rohith',2000])
#     write_data.writerows([['CSK','Dhoni',2009],['RCB','Kohli',2008],['KKR','Murgan',2012],['RR','Sanson',2007],['DC','Pant',2006]])
    
# with open("team_info_append.csv",'a',newline="") as file:
#     write_data=csv.writer(file)
    # # write_data.writerow(['team name','captain','year of incaption'])
    # # write_data.writerow(['MI','Rohith',2000])
    # write_data.writerows([['CSK','Dhoni',2009],['RCB','Kohli',2008],['KKR','Murgan',2012],['RR','Sanson',2007],['DC','Pant',2006]])

# JSON- javascript object notation

import json

# loads-this is for converting the json string into python object..

# json_str='[{"name":"swati","age":30,"city":"new york"}]'  # json string
# print(json_str)
# print(type(json_str))

# converted_object=json.loads(json_str)  # json object to python object
# print(converted_object)
# print(type(converted_object))

# json_str='[{"name":"swati","age":30,"city":"new york"},{"name":"bheem","age":25,"city":"bidar","single":true},{"name":"adarsh","age":20,"city":"sedam","single":false}]'  # json string
# print(json_str)
# print(type(json_str))

# converted_object=json.loads(json_str) 
# print(converted_object)
# print(type(converted_object))

# dumps-

# python_object={"name":"swati","age":30,"city":"new york","single":True,"mobile":None}  # python object

# print(python_object)
# print(type(python_object))

# dumps_object=json.dumps(python_object)  # python object to json object
# print(dumps_object)
# print(type(dumps_object))


# load- its for reading the data from the json file and converting it into python object..

# with open('example_1.json','r') as file:
#      read_data=json.load(file)
#      print(read_data)
#      print(type(read_data))


# dump- its fro writing the  data from the python object into the json files..
    
# with open('example_2.json','w')as file:
#     write_data=json.dump(read_data,file,indunt=4)
#     print(write_data)
#     print(type(write_data))


