counter = 0
total = 0

while True:
    user_input = input('Give me a number:')
    if user_input == 'done':
        break
    try:
        number = float(user_input)
    except:
        print('Invalid input')
        continue
    counter = counter + 1
    total = total + number

print ('total is ',total,'; average is ',total / counter, ' and we have ',counter, 'numbers')

##user_input = input('Give me a number:')
##counter = 0
##total = 0

##Alternative:
##user_input = input('Give me a number:')
##counter = 0
##total = 0
##while user_input != 'done':
##    try:
##        number = float(user_input)
##        counter = counter + 1
##        total = total + number
##    except:
##        number = 'Invalid input'
##        print(number)
##    if number == 'invalid input':
##        continue
##    else :
##        user_input = input('Give me a number:')
##
##print ('total is ',total,'; average is ',total / counter, ' and we have ',counter, 'numbers')
