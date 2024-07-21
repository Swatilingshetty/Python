# # Dictionary : sequence of key:value pair seperated with comma(,) which are declared inside { }..

# dict1 = {"name":"ramesh","city":"hyderabad","email":"ramesh@gamil.com","mobile":"9880553632"}

# print(dict1)
# print(type(dict1))

# accessing inside the dictionary are done using key-name..
# [] - symbol for accessing the dictionary..

# print(dict1['city'])
# print(dict1['mobile'])

# print(dict1['state'])  # This is an error as the key is not present inside the dictionary.

# Dictionary keys are unique
     # even though we have duplicate keys, it wont throw any error, it will consider the latest key:pair into consideration..

# dict1 = {"name":"ramesh","city":"hyderabad","email":"ramesh@gamil.com","mobile":"9880553632","mobile":"7349304818","mobile":"6364451583"}
# print(dict1)

# dict1 = {"name":"ramesh","city":"hyderabad","email":"ramesh@gamil.com","mobile":"9880553632","mobile":["734930481","6364451583"],"pincode":500032,1:11} # it will give error
# print(dict1)

# Dictionaries are mutable:
    # but dictionary values can be any type of data.. 
    # keys should be immutable only..

# dict1 = {"name":"ramesh","city":"hyderabad","email":"ramesh@gamil.com","mobile":"9880553632",}
# print(dict1["city"])

# dict1['city'] = 'mumbai' # if key is already present in the dictionary value to that key is 
# print(dict1)

# dict1["state"] = "maharashtra"  # if key is not present in the dictionary, it will be added as 

# print(dict1)

# nested dictionary:

# dict1 ={"emp_name":"suresh","emp_emial":"suresh@gmail.com","contact":{"primary_no":6364451583,"alternate":9880553632},"address":{"h.no":301,"street":"gachibowli","city":"hyderabad"}}
# print(dict1["address"]["street"])

# print(dict1["contact"]["alternate"])

# dict1["work_location"] = "hyderabad"  # adding new key:value ,we can add only one key value.
# print(dict1)

# print(dir(dict))

# update() : This is for adding the key:value pairs of one dictinary inside other dictionary..

# dict1 ={"emp_name":"suresh","emp_email":"suresh@gmail.com"}
# dict2 ={"work_location":"mumbai","office_address":"plot123,knowledge city,mumbai"}


# print(dict1)
# print(dict2)

# dict1.update(dict2)

# print(dict1)
# print(dict2)

# pop() : its for removing the specific key:value pair from the dictionary..

# dict1.pop("office_address")
# print(dict1)

# # popitem (): it will remove the last key:value pair from the dictionary
# dict1.popitem()  
# print(dict1)

# # clear(): it will clear all the key:values from the dictionary..empty.
# dict1.clear()
# print(dict1)

# get(): it for accessing the values inside the dict using key-name..

# print(dict1.get("emp_name"))
# print(dict1.get("emp_email"))
# print(dict1["emp_name"])
# print(dict1["emp_email"])

# print(dict1.get("state"))
# print(dict1["state"])  # error 

# Keys() : it will return only all the keys inside the dictionary..
# print(dict1.keys())

# # # Values : 
# print(dict1.values())

# # # Items() : it will return all the key:value but each key,value will be retuned as a tuple.
# print(dict1.items())


# copy : its for making the copy of the one dictionary which is assigned with difference memory

# dict1 ={"emp_name":"suresh","emp_email":"suresh@gmail.com"}

# dict2=dict1  # assingning the memory allocation of dict1 with dict2.

# dict2 = dict1.copy()

# print(dict1)
# print(dict2)

# dict2["work_location"] = "bangalore"

# print(dict1)

# print(dict2)

# fromkeys() : its for converting the list of values into dictionary..

# list1 =[1,"name","address","mobile"]

# print({}.fromkeys(list1))

# # setdefault () : setting a default value from the key inside the dictionary if the key is not present inside the dictionary..

# dict1 = {"name":"suresh","email":"suresh@gmail.com"}

# print(dict1)
# print(dict1.setdefault('email',"ramesh@gmail.com"))

# print(dict1.get("state","telangana"))

# # print(dict1)

# print(dict1.get("email"))


# dict1 = {"name":"suresh","email":"suresh@gmail.com","location":"bangalore","state":"karnataka"}

# for ele in dict1:
#     print(ele,dict1[ele])

# for ele in dict1.keys():
#     print(ele)

# for ele in dict1.values():
#     print(ele)

# for key,value in dict1.items():
#     print(key,value)

# for ele in dict1.items():
#     print(ele)

# dict1 = {}

# for ele in range(1,8):
#     dict1[ele] = ele**2

# print(dict1)


# Dictionary comprehension :
# syntax:
# {expression for ele in sequence}
# print({ele:ele**2 for ele in range(1,10)})

# dict1 = {}
# for ele in range(1,10):
#     if ele %2 ==0:  # when we want only even number 
#         dict1[ele] = ele**2

# print(dict1)

# # syntax2 :
# #{expression for ele in sequence if condition}
# print({ele:ele**2 for ele in range(1,10) if ele%2==0})

# syntax3:
#{expression if condition else expression2 for ele in sequence}
# dict1 = {}
# for ele in range(1,10):
#     if ele %2 == 0:
#         dict1[ele]=ele**2
#     else:
#         dict1[ele]=ele**3

# print(dict1)

# # or
# print({ele:ele**2 if ele%2==0 else ele**3 for ele in range(1,10)})

# task

#dict1 ={}
#enter your name:ramesh
# enter your mobile:8494894484848
    
#dict1 = {"ramesh":8494894484848}
# do you want to continue;yes

# enter your name:suresh
# enter your mobile:6364451583
    
# dict1 = {"ramesh":"8494894484848","suresh":"6364451583"}

# do you want to continue;yes

# enter your name : ramesh
#     this user already existed, do you want to add or update:
#         enter your mobile: 7838738738
#         add:
#             dict1 = {"ramesh":["8494894484848","7838738738"],"suresh":"6364451583"}
          #update:
              #dict1 = {"ramesh":"7838738738","suresh":"6364451583"}

dict={"name":"bheti","email":"bheti@12gmail.com","address":"sedol"}
print(dict)
print(type(dict))
print(id(dict))
print(len(dict))