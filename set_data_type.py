
############################ Set  #####################################


# it is a data structure in python that is used to store multiple data type in a single variable
# it is immutable and unchangeable
# not allow duplicate value
# unordered
# example =>  myset = {'apple', 'arif', 'fuad', 3}

myset = {'apple', 'arif', 'fuad', 3}
print(myset)

# set methods are remove, discard, clear , pop, update, max ,min,
# differance, issubset, issuperset, union, intersection

myset = {'apple', 'arif', 'fuad', 3}
myset.remove(3)  # index number
myset.discard(2)
# myset.clear()
myset.pop()
print(myset)

# update method is one kind of add two set just

s = {2,3,4}
s.update(myset)  # here myset is a set and s is a set so update method  add myset with s

s = {'apple', 2, 3, 4, 'arif'}
myset = {'apple', 'arif', 'fuad', 3}
print(s)
print(myset.difference(s))  # remove the all differance value
print(myset.issubset(s))
print(myset.issuperset(s))
print(myset.union(s))  # common and uncommon value
print(myset.intersection(s))  # common value



