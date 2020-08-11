correct_input = False


while not correct_input:
    try:
        t_f = float(input("Enter a temperature in Fahrenheit: "))
        t_c = (5/9) * (t_f - 32)
        print("Temperature %.2f in Fahrenheit is %.2f in Celsius" %(t_f,t_c))
    except ValueError:
        print("Please enter valid integers the Fahrenheit")
    else:
        correct_input = True