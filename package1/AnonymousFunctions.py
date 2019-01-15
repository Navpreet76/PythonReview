"""
Anonymous functions are also called lambda functions in Python because instead of declaring them 
with the standard def keyword, you use the lambda keyword. Check out the following examples:
"""
#Multiplication
double = lambda x: x*2
print double(9)
triple = lambda x: x*3
print triple(9)
quadruple = lambda x: x*4
print quadruple(9)

#Division
half = lambda x: x/2
print half(300)
quarter = lambda x: x/4
print quarter(400)

#Addition
add2 = lambda x: x+2
print add2(20)
add99 = lambda x: x+99
print add99(101)

#Subtraction
subtract2 = lambda x: x-2
print subtract2(100)

subtract99 = lambda x: x-99
print subtract99(101)

#lambdas can be pretty useful as you can see