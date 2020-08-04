import random, statistics

number_one = random.randint(1, 11)
number_two = random.randint(1, 11)
average = number_one + number_two / 2
standard = (statistics.pstdev([number_one, number_two]))

print("The average of", number_one, "and", number_two, "is", average)
print("The standard deviation of ", number_one, "and", number_two, "is", standard)
