import calendar

# Get user input for the year and month
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

# Create a calendar for the given year and month
cal = calendar.monthcalendar(year, month)

# Print the calendar
print(calendar.month_name[month], year)
print("Mo Tu We Th Fr Sa Su")

for week in cal:
    line = ""
    for day in week:
        if day != 0:
            line += f"{day:2d} "
        else:
            line += "   "
    print(line)
