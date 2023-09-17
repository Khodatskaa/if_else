x = float(input(''))
y = float(input(''))
z = float(input(''))

print("choose an operation:")
print("1. max")
print("2. min")
print("3. середньоарифметичне")
choice = input("paste a number of operation(1/2/3): ")

if choice == "1":
    result = max(x, y, z)
    print(result)
elif choice == "2":
    result = min(x, y, z)
    print(result)
elif choice == "3":
    print((x + y + z) / 3)
else:
    print("Unknown operation number")