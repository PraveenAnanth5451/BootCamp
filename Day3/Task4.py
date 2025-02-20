class Animal:
    def __init__(self,name):
        self.name = name

class Cat(Animal):
    def meow(self):
        print(f"Animal'{self.name}' is sounding like meow")
    def purr(self):
        print(f"Animal {self.name} is sounding like purr")

class Dog(Animal):
    def bark(self):
        print(f"Animal'{self.name}' is barking")
    
    def sleep(self):
        print(f"Animal '{self.name}' is sleeping")
    

class hybrid(Cat,Dog):
    def play(self):
        print("{self.name} is playing")


h = hybrid("Praveen")
print(h.bark())
h.purr()
h.meow()
h.sleep()
