# zip function
# The zip() function returns a zip object, which is an iterator of tuples
# where the first item in each passed iterator is paired together,
# and then the second item in each passed iterator are paired together etc.
# zip(iterator1, iterator2, iterator3 ...)
# Iterator objects that will be joined together by the zip method
# zip method combines multiple list into single list
# needed multiple list


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



