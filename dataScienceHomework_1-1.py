import random

def isPrime(n) :
    remainder = 1
    for counter in range(2, int(n**0.5)+1):
        remainder = n % counter
        if(remainder == 0) :
            print(n, "is not a prime number")
            return
    print(n, "is a prime number")

n = random.randrange(2, 32768)
isPrime(n)