#!/usr/bin/env Python
#Global variable init
init = 1

#Define `plus()` function to accept a variable number of arguments
def plus(*args):
    #Local variable `sum()`
    total = 0
    for i in args:
        total += i
        print total
        
print plus(5,9,23,1)
#Access the global variable
print("this is the initialized value "+ str(init))
    
#Try to access the Local variable
#print("this is the sum "+ str(total))
#The use of the local variable here should throw an error as it is not defined globally and should not be known outside of the function
