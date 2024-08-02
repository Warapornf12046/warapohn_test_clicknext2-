def calculate_change(price):
    change = 1000 - price
    print("จำนวนเงินทอน", change, "บาท")

    denominations = [500, 100, 50, 10, 5, 1]
    for denom in denominations:
        count = change // denom
        if count > 0:
            if denom >= 50:
                print(f"{denom} บาท : {count} ใบ")
            else:
                print(f"{denom} บาท : {count} เหรียญ")
            change %= denom

 
calculate_change(32)