"""
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math

def findPrimeFactors(n):
    primeFactors = []

    while (n % 2 == 0): #divide by 2 until n is odd
        primeFactors.append(2)
        n /= 2

    for i in range(3, round(math.sqrt(n)), 2): #using sieve of eratosthenes as range to limit loop
        while (n % i == 0):
            primeFactors.append(i)
            n /= i

    if (n > 2): #grab remaining number
        primeFactors.append(n)

    return primeFactors

print(findPrimeFactors(600851475143))
