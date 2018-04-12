"""OOP Overview

Discuss the advantages and drawbacks of Object Oriented Programming
in general and in Python

"""

#######################################################################
# Generalization/Specialization

class Animal:
    def breathe(self):
        print('Animal is breathing')

    def play(self):
        print('Animal is playing')
        self.interact()

    def interact(self):
        print('Animal is interacting')

class Dog(Animal):

    def interact(self):
        print('Dog is eating rats')

bebe = Dog()
bebe.interact()

class Cat(Animal):

    def play(self):
        print('Cat is playing')
        self.interact()

zena = Cat()


#######################################################################
# The "real world" is not so neat

class Circle:
    def bounding_box(self):
        "Return a square tangent to the circle at exactly four points"
        pass

class Ellipse(Circle):
    "A kind of circle with a viewing angle"

    def bounding_box(self):
        raise NotImplementedError


#######################################################################
# Multiple Inheritance

class Car:
    trunk = 1

class Plane:
    wings = 2

class FlyingCar(Car, Plane):

    def steering_wheel_or_joystick_or_pedals(self):
        pass