#simplecalculator
n1 = int(input('Enter first number:\n'))
n2 = int(input('Enter second number:\n'))

operations = input('Choose operation from Add, Subtract, Multiply, Divide:\n')
if operations == 'Add':
    result = n1 + n2
    print(result)
elif operations == 'Subtract':
    result = n2 - n1
    print(result)
elif operations == 'Multiply':
    result = n1 * n2
    print(result)
else:
    result = n2/n1
    print(result)
