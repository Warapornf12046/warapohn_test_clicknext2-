def sort_numbers ():
    numbers = [] 
    print("โปรดป้อนตัวเลข 10 ตัว:")
    for i in range(10):
        num = int(input(f"ตัวเลขที่ {i + 1}: "))
        numbers.append(num)
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers

sorted_numbers = sort_numbers ()
print("ตัวเลขที่เรียงลำดับจากน้อยไปมากคือ:", sorted_numbers)