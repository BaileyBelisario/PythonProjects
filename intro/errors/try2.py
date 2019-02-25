

try:
    num = int(input('Please enter a number: '))
except:
    print('That is not a number!')
else:
    print('I am in the else')
finally:
    print('Runs no matter what')


