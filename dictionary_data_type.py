############################ Dictionary #####################################

# dictionary is a data structure in python that is store multiple data type data in single variable through key pair value.

# known as an associative array
# used to store data value in key: value pair
# ordered [ use key for indexing ]
# changeable
# not allow duplicate value
# mutable
#  len , value, key , items, copy, setdefault("", "") methods

# can not slicing in dictionary cause there is no specific index . index is build a custom key

dic = {'1': 'arif', '2': 'adnan', '3': 'mustafiz'}  # string key
print(dic['1'])


dic = {1: 'arif', 2: 'adnan', 3: 'must'}  # integer key

print(dic[2])

# value method for show the dictionary value
print(dic.values())

#  key method for show the key
print(dic.keys())

# items method for key and values show
print(dic.items())

# copy method
new_D = dic.copy()
print(new_D.items())

# setdefault method for add new key pair value
dic.setdefault(4, 'fuad')
print(dic.items())

dic1 = {'1': 'arif', '2': 'adnan', '3': 'mustafiz', '1': 'arif'}  # duplicate value not allow
print(dic1.items())