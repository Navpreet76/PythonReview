import random
import sys
n = random.randint(1,99)
guess = int(raw_input("Enter an Integer between 1 and 99: "))
while n!= "guess":
    print
if guess < n:
    print "Guess is too low"
    guess=int(raw_input("Enter an Integer between 1 and 99: "))
elif guess > n:
    print "Guess is too High"
    guess=int(raw_input("Enter an Integer between 1 and 99: "))
else:
    print "You Guessed it!!! Great Job!!!"
sys.exit()
print 

#This file seems to go into an infinite loop when given a guess, figure out why this is happening
    