
########################## while loop ########################
#   initialization
#   while condition
#   statement
#   update

i = 0
while i <= 6:
    print('I am statement of ', i)
    i = i+1

sum = 0
i = 0
while i <= 5:
    sum = sum+i
    i = i+1
print(sum)

# for loop

string = 'arif hossain'
for i in string:
    print(i)


# range is a built in function in python ,
# it is used when a user needs to performs an action for a specific number of time
# performs number of time on any action

a = 5
for i in range(a):
    print(i)


i = 1
while i<=10:
    print(i)
    i+=1
    if i == 5:
        break  # jum the code scope
print('Hello')


i = 1
while i <= 10:
    i = i+1
    if i == 5:
        continue  # skip the iteration
    print(i)


