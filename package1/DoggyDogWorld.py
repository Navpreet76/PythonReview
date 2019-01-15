class Dog:
    """
    Requires:
    Legs - So that the Dog can walk.
    Color - Color of the Dog's fur.
    
    """
    def __init__(self, legs, color):
        self.legs = legs
        self.color = color
    def bark(self):
        bark = " bark " * 2
        return bark    
if __name__ == "__main__":
    dog = Dog(4, "Black & Tan")
    bark = dog.bark()
    print(bark)    