def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    
    return f"{hours:02}:{minutes:02}:{secs:02}"

total_seconds = int(input("กรอกจำนวนวินาที: "))
formatted_time = convert_seconds(total_seconds)
print(formatted_time)
