week_day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print(week_day)

week_end = ["Saturday", "Sunday"]
print(week_end)

day = week_day + week_end
print(day)

sort_day = sorted(day)
print(sort_day)

reverse_day = reversed(day)
print(list(reverse_day))

last_two_day = day[-2], day[-1]
print(last_two_day)
