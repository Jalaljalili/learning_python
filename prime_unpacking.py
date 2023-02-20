#Packing
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

# unpacking
import matplotlib.pyplot as plt

def draw_dot (**dot):
    plt.plot([dot['x']], [dot['y']], 'ro')
    plt.axis([-20,20,-20,20])
    plt.grid()
    plt.axhline(0,color='blue')
    plt.axvline(0,color='blue')
    return plt

p = draw_dot(x=5, y=15)
p.show()
