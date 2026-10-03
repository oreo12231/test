import math
a, b = map(float, input("Welcome to the Math Operations Program! Please enter two numbers separated by a space: ").split())
def sum_result(a, b):
    return a + b
print("The sum of {} and {} is: {}".format(a, b, sum_result(a, b)))
def difference_result(a, b):
    return a - b
print("The difference of {} and {} is: {}".format(a, b, difference_result(a, b)))
def multiplication_result(a, b):
    return a * b
print("The product of {} and {} is: {}".format(a, b, multiplication_result(a, b)))

def division_result(a, b):
    if b == 0:
        print("Division by zero is not allowed!")
        return None
    return a / b
print("The division of {} by {} is: {}".format(a, b, division_result(a, b)))
