from math import sqrt

def primes (*numbers):
    prime_numbers = []
    for n in numbers:
        prime = True
        for i in range (2, int(sqrt(n))+1):
            if not n % i :
                prime = False
                break
        if prime:
            prime_numbers.append(n)
    return prime_numbers


print (primes (10,11,12,13,17,23,199999,1999999))