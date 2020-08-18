month = ("January", "February", "March", "April", "May", "June", "July",
         "August", "September", "October", "November", "December")
days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

in_month = input("Enter month: ")
daysmonth_dict = dict(zip(month, days))

print(f"Number of days in {in_month} is {daysmonth_dict[in_month]}")
