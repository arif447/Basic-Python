print('if u want to break the loop press the upto 5 ')
while True:
    num = input('Enter a number -- ')
    if num == 2:
        print('Number Two')
    elif num == 3:
        print('The number three')
    elif num == 1:
        print('The number one')
    elif num == 4:
        print('The number four')
    elif num == 5:
        print('The number five ')
    else:
        if int(num)> 5:
            print('The number ', num)
            break
# switch statement not abilable in python

