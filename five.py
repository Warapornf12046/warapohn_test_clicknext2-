n1 = int(input('input number : '))
num = 1
for i in range(n1):
    for x in range(n1 - (i+1)):
        print(" ", end=" ")
    for j in range(i + 1):
        print(num % 10," ", end=" ")
        num += 1
    print()