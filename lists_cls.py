# list : sequence of elements seperated with comma(,) which are declared inside [ ]..

# list1 = [32,4.5,"swati","chiru",43,3,2]

# accessing the elements inside the list is done using indexing..

# indexing starts from 0.

#[ ] are used for indexing...

# print(list1[0])

# print(list1[6])

# print(list1[1:5])

# print(list1[0:6:2])

#negative indexing : performing the indexing in reverse order..
# its starts from -1..

# list1 = [32,4.5,"swati","chiru",43,3,2]

# print(list1[-0])
# print(list1[-1])

# print(list1[-5])

# print(list1[-2:-6])  # - as we havenot specified the as negative.

# print(list1[-2:-6:-1])  #[3,43,'chiru','swati'] as we are specifying -1 jumps..

# print(list1[-1:-8:-1])
# print(list1[-1:-4:-2])
# print(list1[-2:-6:-1])

# print(list1[::-1])
# print(list1[::-2])
# print(len(list1))

list2 = [43,'balayya',4.5,[11,12,13,'django'],54]

# # nested list : declaring the list inside other list elements..

# # nested indexing : performing the indexing on other indexing outputs.

# print(list2[1])

# print(list2[1][2])

# print(list2[3][3][-1])  # 0 

# list are mutuable : which we can make the changes after the declaration..

# list2 = [43,'balayya',4.5,[11,12,13,'django'],54]

# print(list2)

# print(id(list2))
# list2[0] = 44

# print(list2)
# print(id(list2))


# del list2[-3]

# print(list2)

# print(id(list2))

#basic operation 
# concatination : adding 2 list elements into single list.
# repeatation : repeating the elements inside the list multiple number of times.

# a = [1,2,3,4]

# b = ['python','django',4.5]

# print(a+b)

# print(b+a)

#repeatation: repeating the elements inside the list multiple number of times..

# print(a*3)

# lists methods:

# print(dir(list))

# adding methods.
 # append
# extend
 # insert

# removal methods :
     # remove
     # pop
     # clear

# Accessing methods: just accesssing the elements and give output
    # index
    # count

#Altering methods: 
   # sort()
   # reverse()
   # copy()


#APPEND : 
# a=[34,'python',4.5,[31,32,'django'],87]
# print(a)

# a.append(43)
# print(a)

# a.append("Balayya")
# print(a)

# a.append([102,421,198])
# print(a)

# append can take only 1 elements at a time and EXTEND can adding multiple elements a time.

# Extend : its for adding multiple elements at a time into the list which takes only sequence data.

# when we are extend we cannot take direct integer or float..

# a.extend(34) # this is an error

# a.extend("python")

# print(a)

# a.extend({"name":"swati","mobile":98765443})  #dictionary(accept only keys)

# print(a)

# mobile = ["98765",'65432','9876655']
# mobile2 = ["09987665",'989765432','876543']

# mobile.append(mobile2[0])
# mobile.append(mobile2[1])
# mobile.append(mobile2[2])

# print(mobile)

# mobile.extend(mobile2)

# print(mobile)

# Insert : it for adding the single element at a time into the list at the specific index location.

# a=[34,'python',4.5,[31,32,'django'],87]

# print(a)

# a.insert(1,'datascience')

# print(a)

# a.insert(4,'swati')

# print(a)

# indexs = [2,3,5]
# values = ["devops","fullstack","salseforce"]

# for b in indexs:
#     a.insert(b,"data")

# print(a)

# Append and Insert bothe are same but only difference is append will add at the last but insert will add at the specific index that we are going to spicified ..

# REMOVAL METHODS : 
# removal () : its for removing the element from the list.

# print(a)

# a.remove('datascience')

# print(a)

# this is for checking wheather element is present in the list or not..
# if 'datascience' in a:   # condition statement
#     a.remove('datascience')

# print(a)

# pop : its also for removing the element from the list but using index value..

# a.pop(4)

# print(a)

# ACCESSING METHODS :
# Index() : it will give the index of an element inside the list..

# a = ['python','43',43,[101,'datascience','43'],43]

# print(a.index(43))

# print(a.index('43'))

# print(a[3].index('43'))

# count() : how many times an element is repeated inside the list..

# print(a.count(43))


# Altering methods :

# Reverse:

# a = ['python','43',43,[101,'datascience','43'],43]

# print(a)

# a.reverse()  #its for reversing the elements in the list.

# print(a)

# sort : its just sorting the value int the list into proper order(ascending or descending order)

# a = [646,87,98,43,65,76,87,8,'python']
# a.sort() : this will returns the error as list contact different datatype values.

# print(a)

# a.sort()
# print(a)

# a = [646,87,98,43,65,76,87,8,]

# print(a)

# # a.sort()
# # print(a.sort())  # it will return none st the output

# # print(a)

# a.sort(reverse=True)
# print(a)

# copy : its for creating the copy of values with the main list..

# list1 =[43,'python','django',45,6,12,'devops']

# list2=list1

# print(list1)
# print(list2)

# print(id(list1))
# print(id(list2))

# list2.append(54)

# print(list1)

# print(list2)

# list2=list1.copy()

# print(id(list1))

# print(id(list2))

# list1 =[43,'python','django',45,6,12,'devops']

# Iterations on the list:

# list1 = ['9008724717','7349304818','6364451583','9606817156','9880553632','7619307559','65432187997','987654322111',]

# # for ele in list1:
# #     print(ele)

# # for ele in list1:
# #     print(len(ele))

# valid_number=[]
# for ele in list1:
#     if len(ele)==10 and ele.startswith('9'):
#        valid_number.append(ele)

# print(valid_number)  

# list comprehension :
# 1st syntax
# [expression for ele in74 sequence]

# list1 = [74,84,76,29,92,17,19,84,74]

# list2 = []

# for ele in list1:
#     list2.append(ele%5)

# print(list2)

# list3 = [ele%5 for ele in list1]  #(in one line code)
# print(list3)


# list1 = [71,748,64,75,86,52,86,96,23]

# list2 = []

# for ele in list1:
#     if ele%2==0:
#         list2.append(ele)
#     else:
#         list2.append(ele+1)
# print(list2)

# 3rd syntax of list comprehension
#[expression if condition else expression for ele in sequence]

# print(ele if ele%2==0 else ele+1 for ele in list1)