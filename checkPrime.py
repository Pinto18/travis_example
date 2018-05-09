import math

def check(num):
    isPrime = False
    if num <= 1:
        return isPrime
    for index in range(2, math.ceil(math.sqrt(num))):
        isPrime = True
        if num % index == 0:
            isPrime = False
            return isPrime
    return isPrime
