#checkprimenumber
number = int(input('Enter your number:\n'))

if number == 1:
    print('Not a prime number')
else:
    for i in range(2, int(number/2)+1):
        if number % i == 0:
            print('Not a prime number')
            break
    else:
        print('PRIME!')
