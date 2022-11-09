
# String slicing and method  ##
# slicing , len, count, index, find, lower , upper , isdigit,isnumeric, isascii
# isdecimal, isspace, isalnum, isalpha, capitalize, center, endwith, startwith, title
# swapcase, replace , split, join  methods


# Here [:] first part is remove part second part is display part
# space is must count

string = 'arif hossain'
a = string[2:6]
print(a)
print(string[0:6])
mid = len(string)//2
print(string[mid:])  # here remove the mid value 6 and show the after mid value 6
print(string[mid-1:mid+2])  # 3 value will be print hos
print(string[:mid:])  # will be show first 6 value
print(string[len(string)-1])  # will be show last value of string
print(string[-1])  # will be show last value of string


# count method is used to count character or substring in a main staring

# print(string.count('substring', start , last_index))

string = 'arif hossain'
print(string.count('ss'))
print(string.count('s'))
print(string.count('is'))  # no value cause the value is out of string
print(string.count('if'))
print(string.count('if', 0, 8))
print(string.count('if', 3, 8))   # no value cause out of index


# index method. it is used to find the index of substring
# string.index('character', start, endindex)
print(string.index('if'))
print(string.index('in'))
print(string.find('s'))  # like index method


print(string.lower())

print(string.upper())

print(string.isdigit())

print(string.isalnum())

print(string.isalpha())

print(string.capitalize())  # capitalize the first character of string


# print(string.center(length, character )) # here length will be big size from the string length
print(string.center(14, '*'))


# print(string.endswith('character', start, end_index))
print(string.endswith('s'))

print(string.startswith('a'))

print(string.title())  # lower to upper just first latter
print(string.swapcase())  # full string upper to lower and lower to upper

# Replace method
# it is used to replace a substring in a string with another substring
# string.replace(old_string, new_string)

string = 'arif hossain'
old = 'hossain'
new_string = 'mahmud'
print(string.replace(old, new_string))

# split method
# This method is used to split or break a string into pieces and return a list
#
print(string.split())
print(string.split('_'))

# Using separator
a = 'arif-hossain-if-hh-ff'
print(a.split('-'))


# join method
# The join() method takes all items in an iterable and joins them into one string.
# "separator".join(value)
list1 = ['a', 'f', 'f', 'j']
print("#".join(list1))
print("".join(list1))



