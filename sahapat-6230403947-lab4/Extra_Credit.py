try:
    user = input("Enter the list of numbers (delimited by a comma): ").split(', ')
    userList = user
    print(userList)

    userindex = int(input("Enter an index: "))
    print(userList[userindex])

except IndexError:
    print(f"The list has no element at index {userindex}")