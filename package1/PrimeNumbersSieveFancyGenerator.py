import itertools
from timeit import itertools

def iter_primes():
    #an iterator of all numbers between 2 and +infinity
    numbers = itertools.count(2)
    
    #generate primes forever
    while True:
        #get the first number from the iterator(always a prime)
        prime = numbers.next()
        yield prime
       #this code iteratively builds up a chain of 
       #filters...slightly tricky, but worth pondering
    numbers = itertools.ifilter(prime.__rmod_,numbers)
for p in iter_primes():
    if p > 1000:
        break
    print p       