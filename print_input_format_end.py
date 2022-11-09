print('arif')
variable = 'Arif Hossain'
Variable = 222
print(variable, '\n', Variable)  # This is case sensitive

print(' My name is', variable, '\n', 'My id number is', Variable)

# The use of Input Function
string = input("enter the string--- ")
integer = int(input("enter the integer--- "))
float_number = float(input("Enter the float--- "))
print(' String = ', string, '\n', 'Integer= ', integer, '\n', 'Float = ', float_number)


# The use of float value print
f = float(input('Enter a float value-- '))
print('The value is % .2f' %f)

print(type(f))
print(type(string))
print(type(integer))

# The use of string format method
# The format() method formats the specified value(s) and insert them inside the string's placeholder.
# The placeholder is defined using curly brackets: {}.
name = 'arif'
roll = 33
phone = 9837
print('My name is {0} and roll is {1} last one my  phone number {2}'.format(name, roll, phone))

a = 44
b = 44
print(f'{a} + {b} = {a+b}')

# concatenation
# concatenation means joining end to end between two string and return a new string

a = 44
b = 44
print(a+b)
s = 'arif'
s1 = 'hossain'
s2 = 33
print(s+s1)
print(s+s2)  # an only concatenate str (not "int") to str
print(s+str(s2))


# The “end” is a keyword that is used in python to place a space after the displayed string instead of a newline.
#  In python every time you print(“something”), by default it will append a newline.
# used to add any string
s = 'arif'
s1 = 'hossain'
# with out end
print(s,)
print(s1)

# with end
print(s, end=" ")
print(s1)

a = 10
for i in range(0, 11, 1):
    print(i, end=" ")

