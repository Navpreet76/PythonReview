"""
Required Arguments of a UDF are those that have to be in there. These arguments need to be PASSED
during function call and in exactly the right order, just like the following example:

"""
#Define `plus()` with the required arguments
def divide(a,b):
    return a/b
#divide() with no args would give an error as the args are required
#divide(9) with one arg would also not work as it needs two args present
print divide(300, 10)
#should work just fine
