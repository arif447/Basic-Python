
def monday():
    return "monday"
def tuesday():
    return "tuesday"
def wednesday():
    return "wednesday"
def thursday():
    return "thursday"
def friday():
    return "friday"
def saturday():
    return "saturday"
def sunday():
    return "sunday"
def default():
    return "Incorrect day"

switcher = {
    1: monday,
    2: tuesday,
    3: wednesday,
    4: thursday,
    5: friday,
    6: saturday,
    7: sunday
    }

def switch(dayOfWeek):
    return switcher.get(dayOfWeek, default)()

print(switch(3))
print(switch(5))


def getinput():
    num1 = int(input('enter the first number == '))
    num2 = int(input('enter the first number == '))
    return num1, num2

def add():
    x, y = getinput()
    return x + y

def sub():
    x, y = getinput()
    return x - y

def div():
    x, y = getinput()
    return x // y

def mul():
    x, y = getinput()
    return x * y

print(" 1- add \n 2- sub \n 3- div \n 4- mul ")

choice = int(input('Enter your choice-- '))
operation = [add, sub, div, mul]
output = operation[choice-1]()
print(output)



