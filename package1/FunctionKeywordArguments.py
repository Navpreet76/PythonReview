"""
If you want to ensure that you call the parameters in the right order, you can use the keyword arguments IN
your function call. You use these to identify the arguments by their parameter name. Example of this is as follows
"""
#define `plus()` function
def plus(a,b):
    return a + b
#Call `plus()` function with parameters
print plus(3,4)
#Call `plus()` fucntion with keyword arguments
print plus(a=19, b=30)
"""
By using keyword arguments, you could switch around the order and still get the same result
"""
print plus(b=30, a=19)

"""
Variable number of Arguments - These are situations where you might not know the exact number of arguments that you want to 
pass to a function. you can do this with the following syntax with *args:
"""
def multipleArgs(*args):
    return sum(args)
#Calculate the Sum
print multipleArgs(1,9,72,201,21,33,18,32)
#You could actually replace the word args with almost anything else, as long as it has the * before it, it should work
#check out the following example
def whateverArgs(*whatever):
    return sum(whatever)
print whateverArgs(39,20,10,100,32,35,21,19,33)
#works the same way
"""
Define `plus()` function to accept a varible number of arguments without using the built in sum function
"""
def addition(*args):
    total = 0
    for i in args:
        total += i
        print total
#Calculate the sum
addition(1,2,5,40,60)
