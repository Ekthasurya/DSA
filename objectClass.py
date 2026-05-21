# Classes and Object in Programming

# Class
# A class is a blueprint or template used to create objects. It defines the structure that specifies the data members (attributes) and functions (methods) an object will contain. A class typically contains two main components:

# 1. Attributes (Data Members): Attributes are the properties or characteristics of an object. They store information related to the object.

# 2. Methods (Functions): Methods define the actions or behaviors that an object can perform.

# Features of a Class

# Describes the data and operations related to a particular entity.
# Serves as a reusable template from which multiple objects can be created.
# Helps organize code by grouping related variables and functions.
# Supports modular programming, making programs easier to understand and maintain.

class Car:

    # Attribute
    def __init__(self, color, model):
        self.color = color
        self.model = model

    # Method
    def start_engine(self):
        print("Engine started")


# Object
# An object is an instance of a class. It represents a real-world entity created using the class blueprint

# Stores actual values for class attributes.
# Allows you to call methods defined in the class.
# Multiple objects can exist from the same class, each holding different data.


# Define a class
class Car:

    # Method: constructor (optional)
    def __init__(self):
        self.color = ""
        self.model = ""

    # Method: starts the engine
    def startEngine(self):
        print(f"{self.model} engine started")

    # Method: stops the engine
    def stopEngine(self):
        print(f"{self.model} engine stopped")

if __name__ == "__main__":

    # Create first car object
    myCar = Car()
    myCar.color = "Red"
    myCar.model = "Toyota"

    # Use attributes and methods
    print("My car color:", myCar.color)
    myCar.startEngine()
    myCar.stopEngine()