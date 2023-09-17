x = float(input(''))
y = float(input(''))

print("choose an operation:")
print("1. сума")
print("2. різниця")
print("3. середньоарифметичне")
print("4. добуток")
choice = input("paste a number of operation(1/2/3/4): ")

if choice == "1":
    print(x + y)
elif choice == "2":
    print(x - y)
elif choice == "3":
    print(x + y / 2)
elif choice == "4":
    print(x * y)
else:
    print("Unknown operation number")



