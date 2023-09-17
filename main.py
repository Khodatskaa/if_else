x = int(input(''))

print('choose an option')
print('1. miles')
print('2. inches')
print('3. yards')
choice = input('paste a number of operation(1/2/3): ')

if choice == '1':
    print(x * 0.000621)
elif choice == '2':
    print(x * 39.37)
elif choice == '3':
    print(x * 1.093)
else :
    print('Unknown operation number')