def factorial(num):

    if (num <= 1):
        return 1
    return num * factorial(num - 1)
num = int(input("Enter the number: "))

print("The factorial of {} is: {}".format(num,factorial(num)))
