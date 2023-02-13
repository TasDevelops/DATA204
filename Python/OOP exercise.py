""" 

4 pillars of OOP 

1. Abstraction in python is defined as a process of handling complexity by hiding unnecessary information from the user.
This is one of the core concepts of object-oriented programming (OOP) languages.
That enables the user to implement even more complex logic on top of the provided abstraction 
without understanding or even thinking about all the hidden background/back-end complexity.



2. Encapsulation refers to the bundling of attributes and methods inside a single class.
It prevents outer classes from accessing and changing attributes and methods of a class. 
This also helps to achieve data hiding.


3. Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.


4. Polymorphism in python defines methods in the child class that have the same name as the methods in the parent class.
In inheritance, the child class inherits the methods from the parent class.
Also, it is possible to modify a method in a child class that it has inherited from the parent class."""
# a class can function to create a blueprint to create objects, we can assign attributes(what descrivbes what the object is) and methods (what each object can do)
#abstract class = a class which contains on or
# abstract method = a method that has a decleration but does not have implementation


from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def __init__(self, make,model,year):   #init method is called everytime you create a new instance of the class. first argument to this method is the word self, which is a reference to the new object that is being created. you can also add other arguments after it. 
        self.make = make  # storing these values to fields in the object
        self.model = model #instance variable
        self.year = year
        
        
    def ShowDescription(self):
        print('This' ,self.make,'is so beautiful')
class Motorcycle(Vehicle):
    def __init__(self, make,model,year, colour):
        self.colour = colour
        super().__init__(make, model,year) # Inherited from the Vehicle Parent


    def speed(self):
        print ('This ' +self.make+ ' is speeding') 

    def stop(self):
        print('This ' +self.make+ ' is stopping')


class Truck(Vehicle):
    def __init__(self, make,model,year, new):
        self.new = new
        super().__init__(make, model,year) # Inherited from the Vehicle Parent

    def GetColour(self):
        print('This' ,self.make, ' is a' ,self.model, 'and it was made in ' ,self.year)


vehicle1 = Vehicle('Mercedes', 'Series one', 2022)
vehicle2 = Vehicle('Toyata', 'Yaris', 2020)
motorcycle1 = Motorcycle('Harley Davidon', 'Nightster',1995, 'Red')
motorcycle2 = Motorcycle('Dutti', 'Panigale',2015, 'Blue')
truck1 = Truck('BMW', 'fiver', 1980, 'Yes')




# calling method 1
#vehicle1.ShowDescription()
#motorcycle1.ShowDescription()
truck1.GetColour()


#vehicle2.speed() #calling speed method

  
