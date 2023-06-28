"""
 Method overriding is a feature in object-oriented programming languages that allows a subclass to provide
 a different implementation of a method that is already defined in its superclass.
"""
class Animal:
    def speak(self):
        print("I'm an animal")

class Dog(Animal):
    def speak(self):
        print("woof")


animal = Animal()
animal.speak()

dog = Dog()
dog.speak()
