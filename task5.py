def is_leap(year):
    leap = False
    
    # If the year is divisible by 4
    if year % 4 == 0:
        # If the year is divisible by 100
        if year % 100 == 0:
            # If the year is divisible by 400
            if year % 400 == 0:
                leap = True
        else:
            leap = True
    
    return leap

year = int(input("Enter the year: "))
print(is_leap(year))
