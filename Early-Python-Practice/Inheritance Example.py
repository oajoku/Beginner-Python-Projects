class Person:
    description="general person"

    def _init_(self,name,age):
        self.name=name
        self.age=age
    def speak(self):
        print("My name is {} and I am {} years old".format(self.name, self.age))
    def eat(self,food):
        print("{} eats {}".format(self.name,food))
    def action(self):
        print("{} jumps".format(self.name))

class Baby(person):
    description="baby"
    def speak(self):
       print("ma ma")
    def nap(self):
       print("{} takes a nap".format(self.name))
person=Person("Carey", 45)
person.speak()
person.eat("crab")
person.action()

baby=Baby("Mia",2)
baby.speak()
baby.eat("Baby Food")
baby.action()
print(person.description)
print(baby.description)
      
