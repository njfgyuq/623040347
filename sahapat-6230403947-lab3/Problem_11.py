while True:
    try:
        one = float(input("Enter the first number: "))
        if one == "quit":
            break
        two = float(input("Enter the second number: "))
        if two == "quit":
            break
        operator = str(input("Enter the operator: "))
    except ValueError:
        break
    if operator == "+":
        print(f"{one} + {two} = "
              f"{one + two}")
    elif operator == "-":
        print(f"{one} - {two} = "
              f"{one - two}")
    elif operator == "*":
        print(f"{one} * {two} = "
              f"{one * two}")
    elif operator == "/":
        if one == 0 or two == 0:
            print("Cannot divide a number by 0")
        else:
            print(f"{one} / {two} = "
                  f"{one / two}")
    elif operator == "quit":
        break
    else:
        print("Unknown operator")
