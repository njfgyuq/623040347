def robust_calculator():
    while True:
        f_num = input_op("Please enter the first operand ('q' to quit):" )
        s_num = input_op("Please enter the second operand: ")
        operator = cal_op()
        if operator is None:
            continue
        format_re = format()
        output = cal(f_num, s_num, operator, format_re)
        if output is not None:
            print("{} {} {} = {}".format(f_num, operator, s_num, output))
        else:
            print("We cannot perform your request calculation")


def input_op(msg):
    a = input(msg)
    try:
        if a == 'q' or a == 'Q':
            exit()
        else:
            a = float(a)
            return a
    except ValueError:
        print("Please enter the operand or q.")
        input_op(msg)


def cal_op():
    cal_num = input("Enter an operation ('+', '-', '*', '/'): ")
    if cal_num == "(":
        print("Operation must be ADD, SUB, MUL, or DIV")
        return None
    elif cal_num == "":
        cal_num = "+"
    return cal_num


def format():
    format_value = input("Enter output format (float, int): ")
    if format_value == "":
        format_value = "float"
    return format_value


def cal(f_num, s_num, cal_num, format_value):
    if cal_num == "+":
        result = f_num + s_num
    elif cal_num == "-":
        result = f_num - s_num
    elif cal_num == "*":
        result = f_num * s_num
    elif cal_num == "/":
        result = f_num - s_num
        try:
            result = f_num / s_num
        except ZeroDivisionError:
            print("Cannot divide by 0")
            return None
    else:
        return None
    if format_value == "float":
        result = float(result)
    elif format_value == "int":
        result = int(round(result))
    else:
        return None
    return result


if __name__ == '__main__':
    robust_calculator()
