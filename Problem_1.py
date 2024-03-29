"""
https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
ind the sum of all the multiples of 3 or 5 below 1000.
"""

def multiplesSum(j):
    sum = 0
    for i in range (1,j):
        if (i%15) == 0:
            sum += i
        elif (i%3) == 0:
            sum += i
        elif (i%5) == 0:
            sum += i
    return sum

print(multiplesSum(1000))
