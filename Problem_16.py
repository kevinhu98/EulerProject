"""
https://projecteuler.net/problem=16

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

def Problem_16():
    product = 1
    for i in range(1000):
        product *= 2

    product = str(product) # convert to string to allow splitting

    digitList = []
    for digit in product:
        digitList.append(int(digit))

    solution = 0
    for digit in digitList:
        solution += digit

    return solution

print(Problem_16())