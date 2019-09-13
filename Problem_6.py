"""
https://projecteuler.net/problem=6


Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def Problem_6(n):
    sumOfSquares = 0
    sumToSquare = 0

    for i in range(1, n+1):
        sumToSquare += i
        sumOfSquares = sumOfSquares + (i*i)

    sumToSquare *= sumToSquare

    return (sumToSquare - sumOfSquares)

print(Problem_6(100))
