# print('arif')
# variable = 'Arif Hossain'
# Variable = 222
# print(variable, '\n', Variable)  # This is case sensitive
#
# print(' My name is', variable, '\n', 'My id number is', Variable)
#
# # The use of Input Function
# string = input("enter the string--- ")
# integer = int(input("enter the integer--- "))
# float_number = float(input("Enter the float--- "))
# print(' String = ', string, '\n', 'Integer= ', integer, '\n', 'Float = ', float_number)
#
#
# # The use of float value print
# f = float(input('Enter a float value-- '))
# print('The value is % .2f' %f)
#
# print(type(f))
# print(type(string))
# print(type(integer))
#
# # The use of string format method
# # The format() method formats the specified value(s) and insert them inside the string's placeholder.
# # The placeholder is defined using curly brackets: {}.
# name = 'arif'
# roll = 33
# phone = 9837
# print('My name is {0} and roll is {1} last one my  phone number {2}'.format(name, roll, phone))
#
# a = 44
# b = 44
# print(f'{a} + {b} = {a+b}')
#
# # concatenation
# # concatenation means joining end to end between two string and return a new string
#
# a = 44
# b = 44
# print(a+b)
# s = 'arif'
# s1 = 'hossain'
# s2 = 33
# print(s+s1)
# print(s+s2)  # an only concatenate str (not "int") to str
# print(s+str(s2))
#
#
# # The “end” is a keyword that is used in python to place a space after the displayed string instead of a newline.
# #  In python every time you print(“something”), by default it will append a newline.
# # and add any string
# s = 'arif'
# s1 = 'hossain'
# # with out end
# print(s,)
# print(s1)
#
# # with end
# print(s, end=" ")
# print(s1)
#
# a = 10
# for i in range(0, 11, 1):
#     print(i, end=" ")
#

                                    ##  String slicing and method  ##

                                    # # slicing , len, count, index, find, lower , upper , isdigit,isnumeric, isascii
                                    # # isdecimal, isspace, isalnum, isalpha, capitalize, center, endwith, startwith, title
                                    # # swapcase, replace , split, join  methods



# # Here [:] first part is remove part second part is display part
# # space is must count
#
# string = 'arif hossain'
# a = string[2:6]
# print(a)
# print(string[0:6])
# mid = len(string)//2
# print(string[mid:])  # here remove the mid value 6 and show the after mid value 6
# print(string[mid-1:mid+2])  # 3 value will be print hos
# print(string[:mid:])  # will be show first 6 value
# print(string[len(string)-1])  # will be show last value of string
# print(string[-1])  # will be show last value of string



# #count method is used to count character or substring in a main staring
#
# #print(string.count('substring', start , last_index))
#
# string = 'arif hossain'
# print(string.count('ss'))
# print(string.count('s'))
# print(string.count('is'))  # no value cause the value is out of string
# print(string.count('if'))
# print(string.count('if', 0, 8))
# print(string.count('if', 3, 8))   # no value cause out of index
#
#
# # index method. it is used to find the index of substring
# # string.index('character', start, endindex)
# print(string.index('if'))
# print(string.index('in'))
# print(string.find('s'))  # like index and count method
#


# print(string.lower())
#
# print(string.upper())
#
# print(string.isdigit())
#
# print(string.isalnum())
#
# print(string.isalpha())
#
# print(string.capitalize())  # capitalize the first character of string


# # print(string.center(length, character )) # here length will be big size from the string length
# print(string.center(14, '*'))


# # print(string.endswith('character', start, end_index))
# print(string.endswith('s'))
#
# print(string.startswith('a'))
#
# print(string.title())  # lower to upper just first latter
# print(string.swapcase())  # full string upper to lower and lower to upper

#  Replace method
#  it is used to replace a substring in a string with another substring
#  string.replace(old_string, new_string)
#
# string = 'arif hossain'
# old = 'hossain'
# new_string = 'mahmud'
# print(string.replace(old, new_string))
#
# # split method
# # This method is used to split or break a string into pieces and return a list
# #
# print(string.split())
# print(string.split('_'))
#
# # Using separator
# a = 'arif-hossain-if-hh-ff'
# print(a.split('-'))
#
#
# # join method
# # The join() method takes all items in an iterable and joins them into one string.
# # "separator".join(value)
# list1 = ['a', 'f', 'f', 'j']
# print("#".join(list1))
# print("".join(list1))
#



######################################  List  #######################################################

# # A list is a data structure in python that is mutable (2) changeable (3) allow duplicate value (4) order sequence of elements
# # list are used to store multiple date type data in a single variable
# # list can not handle  arithmetic  operation
# # list methods are len, add, insert, append , pop , remove , clear, reverse, count, in operator , sort, copy, join ,
#
# list1 = [1, 2, 4, 'ARIF', 'F', '44.44']  # here multiple data
#
# print(list1)
#
# # slicing
# print(list1[2:5])  # here index start from zero but string index start from 1
#
# # in kew word or operator
# # it is used to check any value in a list
# # and return true or false
# # print('value' in list1)
# print(2 in list1)
#
# # len
# print(len(list1))
#
# # insert methods -- it is used to insert any value in specific index
# # list.insert(index number, value)
# list1.insert(2, 'Adnan')
# print(list1)


# # Add method
# # it is used to add value in the last index
# list1 = [1, 2, 4, 'ARIF', 'F', '44.44']
# li = list1 + ['karim']
# print(li)

# # Append method is used to add value in the last index
#
# list1 = [1, 2, 4, 'ARIF', 'F', '44.44']
# list1.append('Tarek')
# print(list1)

# # pop method is used to remove last value
# list1 = [1, 2, 4, 'ARIF', 'F', '44.44']
# print(list1.pop())
# print(list1)

# # remove method is used to remove any value according the give index
#
# list1 = [1, 2, 4, 'ARIF', 'F', '44.44']
# list1.remove(1)  # here 1 is index number
# print(list1)

# # reverse method
# list1 = [1, 2, 4, 'ARIF', 'F', '44.44']
# list1.reverse()
# print(list1)
#
# # sort method
# # list1 = [1, 2, 4, 'ARIF', 'F', '44.44']  # this is not supported cause str and int not sorted together
# # list1.sort()
# # print(list1)
# list2 = [3, 99, 4, 666, 1, 44, 0]
# list2.sort()
# print(list2)

# # clear method is used to clear all item
# list2.clear()
# print(list2)
#
# # copy method
#
# list2 = [3, 99, 4, 666, 1, 44, 0]
# list1 = list2.copy()
# print(list1)
#
# # count method is used to count the any object
#
# print(list1.count(4))
#
# # list join method : The join() method takes all items in an iterable and joins them into one string.
#
# a = ''.join(str(list2))  # here convert into str cause list is integer value
# print(a)
# print(type(a))
#
#       ############################### Tuple ####################
# # Tuple is a data structure in python that is used to store multiple data type in a single variable
# # immutable
# # unchangeable
# # duplicate value allow
# # ordered
#
# # example => tuple = ('a', 'n', 2,3,)
# # tuple has just two built in methods that are count, index
#
# t = (3, 4, 5, 'arif')
# print(t)
#
# # slicing
# print(t[:3])
# print(t[:3:])  # 3 is value of total print
#
# # len
# print(len(t))
#
# # index , count and find
# print("count value of : ", t.count(3))
# print("index of = ", t.index('arif'))
#
# # two tuple add
# tuple1 = (1, 2, 4, 'arif')
# tuple2 = ('ar', 'hh', 'arif',)
# tuple3 = tuple1 + tuple2
# print(tuple3)
#
# # immutable data type are tuple, set, int, float, string, boolean, unicode
# tu = ('e', 4, 6)
# tu[1] = 'arif'
# print(tu) # there is an error


############################ Dictionary #####################################

# # dictionary is a data structure in python that is store multiple data type data in single variable through key pair value
#
# # known as an associative array
# # used to store data value in key: value pair
# # ordered [ use key for indexing ]
# # changeable
# # not allow duplicate value
# # mutable
# # slice , len , value, key , items, copy, setdefault("", "") methods
#
# # can not slicing in dictionary cause there is no specific index . index is build a custom key
#
# dic = {'1': 'arif', '2': 'adnan', '3': 'mustafiz'}  # string key
# print(dic['1'])
#
#
# dic = {1: 'arif', 2: 'adnan', 3: 'must'}  # integer key
#
# print(dic[2])
#
# # value method for show the dictionary value
# print(dic.values())
#
# #  key method for show the key
# print(dic.keys())
#
# # items method for key and values show
# print(dic.items())
#
# # copy method
# new_D = dic.copy()
# print(new_D.items())
#
# # setdefault method for add new key pair value
# dic.setdefault(4, 'fuad')
# print(dic.items())

############################ Set  #####################################


# # it is a data structure in python that is used to store multiple data type in a single variable
# # it is immutable and unchangeable
# # not allow duplicate value
# # unordered
# # example => myset = {'apple', 'arif', 'fuad', 3}
#
# myset = {'apple', 'arif', 'fuad', 3}
# print(myset)

# set methods are remove, discard, clear , pop, update, max ,min,
# differance, issubset, issuperset, union, intersection

# myset = {'apple', 'arif', 'fuad', 3}
# myset.remove(3)  # index number
# myset.discard(2)
# #myset.clear()
# myset.pop()
# print(myset)
# s = {2,3,4}
# s.update(myset)
# s = {'apple', 2, 3, 4, 'arif'}
# myset = {'apple', 'arif', 'fuad', 3}
# print(s)
# print(myset.difference(s))  # remove the all differance value
# print(myset.issubset(s))
# print(myset.issuperset(s))
# print(myset.union(s))  # common and uncommon value
# print(myset.intersection(s))  # common value
#



########################## while loop ########################
# # initialization
# #  while condition
# # statement
# #  update
# i = 0
# while i <= 6:
#     print('I am statement of ', i)
#     i = i+1

# sum = 0
# i = 0
# while i <= 5:
#     sum = sum+i
#     i = i+1
# print(sum)

# # for loop
#
# string = 'arif hossain'
# for i in string:
#     print(i)
#
#
# # range is a built in function in python ,
# # it is used when a user needs to performs an action for a specific number of time
# performs number of time on any action

# a = 5
# for i in range(a):
#     print(i)

# i = 1
# while i<=10:
#     print(i)
#     i+=1
#     if i == 5:
#         break  # jum the code scope
# print('Hello')

# i = 1
# while i <= 10:
#     i = i+1
#     if i == 5:
#         continue  # skip the iteration
#     print(i)
#
# print('if u want to break the loop press the upto 5 ')
# while True:
#     num = input('Enter a number -- ')
#     if num == 2:
#         print('Number Two')
#     elif num == 3:
#         print('The number three')
#     elif num == 1:
#         print('The number one')
#     elif num == 4:
#         print('The number four')
#     elif num == 5:
#         print('The number five ')
#     else:
#         if int(num)> 5:
#             print('The number ', num)
#             break
################################################ Function ####################################

## switch statement not abilable in python
# def monday():
#     return "monday"
# def tuesday():
#     return "tuesday"
# def wednesday():
#     return "wednesday"
# def thursday():
#     return "thursday"
# def friday():
#     return "friday"
# def saturday():
#     return "saturday"
# def sunday():
#     return "sunday"
# def default():
#     return "Incorrect day"
#
# switcher = {
#     1: monday,
#     2: tuesday,
#     3: wednesday,
#     4: thursday,
#     5: friday,
#     6: saturday,
#     7: sunday
#     }
#
# def switch(dayOfWeek):
#     return switcher.get(dayOfWeek, default)()
#
# print(switch(3))
# print(switch(5))
#
#
# def getinput():
#     num1 = int(input('enter the first number == '))
#     num2 = int(input('enter the first number == '))
#     return num1, num2
#
# def add():
#     x, y = getinput()
#     return x + y
#
# def sub():
#     x, y = getinput()
#     return x - y
#
# def div():
#     x, y = getinput()
#     return x // y
#
# def mul():
#     x, y = getinput()
#     return x * y
#
# print(" 1- add \n 2- sub \n 3- div \n 4- mul ")
#
# choice = int(input('Enter your choice-- '))
# operation = [add, sub, div, mul]
# output = operation[choice-1]()
# print(output)
#
#

# zip function
# The zip() function returns a zip object, which is an iterator of tuples
# where the first item in each passed iterator is paired together,
# and then the second item in each passed iterator are paired together etc.
# zip(iterator1, iterator2, iterator3 ...)
# Iterator objects that will be joined together by the zip method
# zip method combine multiple list into single list


a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")
x = zip()
x = list(zip(a, b))
print(x)


# unzip
aa = [('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica')]
unzip = list(zip(*aa))
print(unzip)

print("first list--", aa[0])
print("second list--", aa[1])



