class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
        print (f"dog '{self.name}' is barking")
    
    def sleep(self):
        print(f"dog '{self.name}' is sleeping")
    

dog = Dog("Tommy", 5)
dog.bark()
dog.sleep()