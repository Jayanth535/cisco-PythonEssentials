year = int(input("Enter a year: "))

if year < 1582:
	print("Not within the Gregorian calendar period")
elif year%400!=0 & year%4!=0:
    print(year, "is a Common year")
else:
    print(year," is a Leap year")
    
# Sample input:
# 2000
# Expected output:
# Leap year
# Output
# Sample input:
# 1999
# Expected output:
# Common year
# Sample input:
# 1580
# Expected output:
# Not within the Gregorian calendar period