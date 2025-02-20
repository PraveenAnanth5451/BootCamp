class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
        print (f"dog '{self.name}' is barking")
    
    def sleep(self):
        print(f"dog '{self.name}' is sleeping")

class Puppy(Dog):
    def play(self):
        print(f"puppy '{self.name}' is playing in the ground")


p = Puppy("rose",5)
p.bark()
p.sleep()
p.play()