num = int(input('Enter number of rows: '))   

for i in range(num, 0,-1):
    for j in range(num - i):
        print(" ", end="")
    for j in range(2 * i -1):
        print("*", end="")
    print()
