year = int(input("Enter your year: "))

if year%4 == 0:
    if year%100 == 0 and year%400 != 0:  # 1700%400 != 0
        print("This is not a leap year")
    else:
        print("This is a leap year")
else:
    print("This is a not a leap year")