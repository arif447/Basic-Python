

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# [expression for i in list]

lsit1 = [1, 2, 3, 4, 5]
newlist1 = [x*x for x in lsit1]
print(newlist1)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)


list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 5, 7, 7]
newlist2 = [x+z for x in lsit1 for z in list2]  # here list2 fully iterate always for each iteration of list1 ,
print(newlist2)

