import math

# def check(num):
    # isPrime = False
    # if num <= 1:
        # return isPrime
    # for index in range(2, math.ceil(math.sqrt(num))):
        # isPrime = True
        # if num % index == 0:
            # isPrime = False
            # return isPrime
    # return isPrime

def isPrime(num):
    if num < 1:
        return False
    for index in range(2, num - 1):
        if num % index == 0: 
            return False 
    return True 

def main():
    number = int(input("Enter a number to see if it is prime: "))
    if isPrime(number):
        print(number , " is prime.\n")
    else:
        print(number, "is not prime.\n")


if __name__=='__main__':
    main()
