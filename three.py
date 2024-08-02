def display_airing_days(days):
    result = ""
    start = days[0]
    end = days[0]

    for i in range(1, len(days)):
        if days[i] == end + 1:
            end = days[i]
        else:
            if start == end:
                result += str(start) + ", "
            else:
                result += str(start) + "-" + str(end) + ", "
            start = days[i]
            end = days[i]

    if start == end:
        result += str(start)
    else:
        result += str(start) + "-" + str(end)

    print(result)

days1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
display_airing_days(days1)   

days2 = [1, 4, 6, 9, 10, 14, 16, 17]
display_airing_days(days2)   