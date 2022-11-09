# Map function is built in function  in python
# it takes two parameter, one--function , two -- list

def add(a):
    return a*a


value = [1, 2, 4, 5]

result = list(map(add, value))
print(result)


def myfunction(a, b):
    return a+b


list0 = ['A', 'B']
list1 = ['C', 'D']  # like zip function

result = (map(myfunction, list0, list1))
print(list(result))