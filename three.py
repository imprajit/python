year = int(input("Enter the year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("yes! this year is a leap year")
else:
    print("no, this year is not a leap year")
