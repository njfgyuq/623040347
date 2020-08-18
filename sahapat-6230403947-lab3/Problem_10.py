total_sum = 0
divide = 0

while True:
    user = int(input("Enter an integers:"))
    if user > 0:
        divide += 1
        total_sum = total_sum + user
    elif user < 0:
        if divide == 0:
            print("You haven't entered a positive number")
            break
        elif divide > 0:
            print(f"Average is {total_sum / divide}")
        break
