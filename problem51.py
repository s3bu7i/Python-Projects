from datetime import datetime

date1 = input("Enter 1st date \n in this formate m/d/Full year")
date2 = input("Enter 2nd date \n in this formate m/d/Full year")

date_format = "%m/%d/%Y"

d1 = datetime.strptime(date1, date_format)
d2 = datetime.strptime(date2, date_format)
diff  = d2-d1
print("Diff between two days is = "+str(diff.days))