num = int(input('Enter number : '))   

for i in range(1, num+1):
    for j in range(num - i):
        print(" ", end="")
    for j in range(2 * i -1):
        print("*", end="")
    print()

 