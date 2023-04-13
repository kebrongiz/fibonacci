from factorial import factorial


def e_x(power):
    ex = 1

    for value in range(1, 52):
        num = pow(power, value)
        den = factorial(value)
        ex += num/den
    return  ex
print("e^{} = {}".format(5, e_x(5)))

