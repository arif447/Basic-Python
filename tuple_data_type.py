
      ############################### Tuple ####################

# Tuple is a data structure in python that is used to store multiple data type in a single variable
# immutable
# unchangeable
# duplicate value allow
# ordered
# example => tuple = ('a', 'n', 2,3,)
# tuple has just two built in methods that are count, index

t = (3, 4, 5, 'arif')
print(t)

# slicing
print(t[:3])
print(t[:3:])  # 3 is value of total print

# len
print(len(t))

# index , count
print("count value of : ", t.count(3))
print("index of = ", t.index('arif'))

# two tuple add
tuple1 = (1, 2, 4, 'arif')
tuple2 = ('ar', 'hh', 'arif',)
tuple3 = tuple1 + tuple2
print(tuple3)

# immutable data type are tuple, set, int, float, string, boolean, unicode
tu = ('e', 4, 6)
tu[1] = 'arif'
print(tu)  # there is an error



