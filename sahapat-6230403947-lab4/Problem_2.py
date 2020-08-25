def check_result(msg):
    while True:
        check = str(input(msg))
        try:
            check = int(check)
        except ValueError:
            pass
        else:
            return check
        print("Please enter a number")
while True:
    try:
        one = check_result("Please enter the first operand: ")
        two = check_result("Please enter the second operand: ")
        operator = str(input("Please enter the operator (+, -, *, /): "))

        if operator == "+":
            print(f"Result of {one} + {two} is "
                  f"{one + two}")
        elif operator == "-":
            print(f"Result of{one} - {two} is "
                  f"{one - two}")
        elif operator == "*":
            print(f"Result of{one} * {two} is "
                  f"{one * two}")
        elif operator == "/":
            print(f"Result of{one} / {two} is "
                  f"{one / two}")
        else:
            print("Unknown operator")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    exit()