#Define a function
def plus(a, b):
    return a + b

#Create a Summation Class
class Summation(object):
    def sum(self, a, b):
        self.contents = a + b
        return self.contents
    #Instantiate `Summation` class to call `sum()`
    #sumInstance = Summation()
    #sumInstance.sum(2,8)
    
    #check why Summation is showing as undefined. Python can be so strange at times