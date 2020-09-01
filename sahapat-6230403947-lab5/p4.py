def factorial(x) :
    if x <= 1:
        return 1
    else:
        return (x * factorial(x-1))


try:
    integer_fac = float(input("Enter an integer: "))
    if integer_fac != int(integer_fac):
        raise ValueError("%s is not a positive integer."% integer_fac)
    elif integer_fac < 0:
        raise ValueError("%s is not a positive integer."% integer_fac)
    else:
        integer_fac = int(integer_fac)
except ValueError  as err:
    print("Please enter a positive integer. %s" % err)
else:
    print("Factorial(%d) is " % integer_fac, factorial(x= integer_fac) )
