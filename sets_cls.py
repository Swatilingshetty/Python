
# sets : sequence of elements seperated with comma(,)declared inside { }.which are unordered and contains unique elements.

# set1={43,"python","django",98,(1,2,3),43,98,"python"}   # each output order chnge everytime. and it directly remove the duplicate elements.

# print(set1)

# print(type(set1))

# set is mutable but the elements inside the set should be immutable

# not accessing inside the set as sets sre unorderd..

# sets methods: add,update,copy,pop,remove,clear,

# print(dir(set))

# add: its for adding single elements inside the set at atime.

# set1 = {43,"python",5.6,"django",(11,12,13),43,5.6,43}
# print(set1)

# set1.add(65)
# print(set1)

# set1.add("swati")
# print(set1)

# set1.add("devops")
# print(set1)

# update(): its for adding the multiple elements into the set. it will take only sequence of data.
# print(set1)

# set1.update("python",(11,12,113),[65,6,7])
# print(set1)

# remove():

# set1.remove("python")
# print(set1)

# pop(): it will remove the starting element of set.

# set1.pop(
# clear():

# set1.clear()
# print(set1)

# # empty_)
# print(set1)
# set={}  # not corect it will take it as empty dictionary...
# print(type(empty_set))

# empty_set=set()  #empty set declaration..
# print(type(empty_set))

# set operation:

# union(|)
# intersection(&)
# difference(-)
# symmetric_differnce(^)

# set1 ={43,65,"python",12}

# set2={43,68,"django",32}

# union(|): adding the element of both the sets into single set by removing the duplicates..
# print(set1|set2)
# print(set1.union(set2))

# # intraction(&): common elements between both the sets..

# print(set1.intersection(set2))
# print(set1&set2)

# difference(-): removing the elements from first set which are present in the second set

# set1 ={43,65,"python",12}

# set2={43,68,"django",32}

# print(set2.difference(set1))
# print(set1-set2)

# symmetric_diffrence(^): uncommon elements between both the side..

# print(set1.symmetric_difference(set2))
# print(set1^set2)

# print(set1)
# print(set2)

# intersection_update
# difference_update
# symmetric_update

# set1.intersection_update(set2)
# print(set1)

# set2.difference_update(set1)
# print(set2)

# set2.symmetric_difference_update(set1)
# print(set2)

# set1 = {43,65,"python",12,76}

# set2 = {43,76,"python"}

# print(set1.issuperset(set2))  # true

# print(set2.issuperset(set1))  # false

# print(set1.issubset(set2))
# print(set2)

# isdisjoint(): no common elements between both the sets..

# print(set1.isdisjoint(set2))