
######################################  List  #######################################################

# A list is a data structure in python that is mutable (2) changeable (3) allow duplicate value (4) order sequence of elements
# list are used to store multiple date type data in a single variable
# list can not handle  arithmetic  operation
# list methods are len, add, insert, append , pop , remove , clear, reverse, count, in operator , sort, copy, join ,

list1 = [1, 2, 4, 'ARIF', 'F', '44.44']  # here multiple data

print(list1)

# slicing
print(list1[2:5])  # here index start from zero but string index start from 1

# in kew word or operator
# it is used to check any value in a list
# and return true or false
# print('value' in list1)
print(2 in list1)

# len
print(len(list1))

# insert methods -- it is used to insert any value in specific index
# list.insert(index number, value)
list1.insert(2, 'Adnan')
print(list1)


# Add method
# it is used to add value in the last index
list1 = [1, 2, 4, 'ARIF', 'F', '44.44']
li = list1 + ['karim']
print(li)

# Append method is used to add value in the last index

list1 = [1, 2, 4, 'ARIF', 'F', '44.44']
list1.append('Tarek')
print(list1)

# pop method is used to remove last value
list1 = [1, 2, 4, 'ARIF', 'F', '44.44']
print(list1.pop())
print(list1)

# remove method is used to remove any value according the given index

list1 = [1, 2, 4, 'ARIF', 'F', '44.44']
list1.remove(1)  # here 1 is index number
print(list1)

# reverse method
list1 = [1, 2, 4, 'ARIF', 'F', '44.44']
list1.reverse()
print(list1)

# sort method
# list1 = [1, 2, 4, 'ARIF', 'F', '44.44']  # this is not supported cause str and int not sorted together
# list1.sort()
# print(list1)
list2 = [3, 99, 4, 666, 1, 44, 0]
list2.sort()
print(list2)

# clear method is used to clear all item
list2.clear()
print(list2)

# copy method

list2 = [3, 99, 4, 666, 1, 44, 0]
list1 = list2.copy()
print(list1)

# count method is used to count the any object

print(list1.count(4))

# list join method : The join() method takes all items in an iterable and joins them into one string.

a = ''.join(str(list2))  # here convert into str cause list is integer value
print(a)
print(type(a))
