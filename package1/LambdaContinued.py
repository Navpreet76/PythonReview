from functools import reduce

# `sum()` lambda function
sum = lambda x, y: x+y;

#Calling the anonymous `sum()` function
print sum(5,6)
#Translate to a User Defined Function
def sum1(x,y):
    return x + y
print sum1(12,10)

#You use anonymous function when you require a nameless function for a short period of time and that is created at runtime
#Specific contexts in which this would be relevant is when working with filter(), map() and reduce():
my_list = [1,2,3,4,5,6,7,8,9,10]

#Use Lambda function with `filter()`
filtered_list = list(filter(lambda x: (x*2 > 10), my_list))
print(filtered_list)
testing_list = list(filter(lambda x: (x*2 > 17), my_list))
print(testing_list)

#Use Lambda function with `map()`
mapped_list = list(map(lambda x: (x*2 > 10), my_list))
print(mapped_list)

#Use Lambda function with `reduce()`
reduced_list = reduce(lambda x, y: x+y, my_list)
print(reduced_list)