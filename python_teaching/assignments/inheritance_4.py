# Demonstrate multilevel inheritance by creating three classes:  LivingThing , 
# Animal , and  Dog , where each inherits from the previous. Add a method in Test2
# each class and call all of them from a  Dog  object


class LivingThing:
    def breathes(self):
        print("Yes ! It breathes.")
    
class Animal(LivingThing):
    def have_teeth(self):
        print("Yes! It has teeth.")

class Dog(Animal):
    def bark(self):
        print("Yes! It barks.")

d1 = Dog()

d1.breathes()
d1.have_teeth()
d1.bark()