def factorial(x) :
    if x <= 1:
        return 1
    else:
        return (x * factorial(x-1))


try:
    integer_fac = int(input("Enter an integer: "))
    if integer_fac < 0:
        raise ValueError("{} is not a positive integer.".format(integer_fac))
except ValueError  as err:
    print("Please enter a positive integer. %s" % err)
else:
    print("Factorial(%d) is " % integer_fac, factorial(x= integer_fac) )
