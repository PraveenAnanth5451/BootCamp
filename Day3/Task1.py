class Dog:
    def set(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
        return f"dog '{self.name}' is barking"
    
    def sleep(self):
        print(f"dog '{self.name}' is sleeping")
    

dog = Dog()
dog.set("Tommy", 5)
print(dog.bark())
dog.sleep()