"""
Python UDF's can take four types of arguments

Default Arguments
Required Arguments
Keyword Arguments
Variable Number of Arguments

Default Arguments - are those that take a default value and if no argument value is passed during the function call.
You can assign this default value with the assignment operator =, just like in the following example:

"""
#Define `plus()` function
def plus(a,b = 2):
    return a + b

#Call `plus()` with only `a` param
plus(a=1)

#Call `plus()` with `a` and `b` params
print plus(a=1, b=3)
print plus(a=89, b=11)
print plus(a=99)
