x = float(input(''))
y = float(input(''))
z = float(input(''))

print('choose an operation:')
print('1. сума')
print('2. добуток')
choice = input('paste a number of operation(1/2):')

if choice == '1':
    print(x + y + z)
elif choice == '2':
    print(x * y * z)
else:
    print('Unknown operation number')

