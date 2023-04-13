def fibonacci(num):

    if (num <= 0):
        return 0
    if (num == 1):
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)
num = int(input("Enter the number: "))

print("The fibonacci value at {} is {}".format( num, fibonacci(num)))
