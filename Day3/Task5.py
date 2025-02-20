class Robot:
    def __init__(self,model,energy_level = 100):
        self._model = model
        self.__energy_level = energy_level

    def model(self):
        print(f"Your Computer model is '{self._model}'")
    def get_energy(self):
        print(f"Your energy level is {self.__energy_level}")

    def set_energy(self, new_energy):
        if 0 <=new_energy < 100:
            self.__energy_level = new_energy
            return f"New energy level is {self.__energy_level}"
        else:
            return "You must enter the energy level between limit - 100"
        
    def charge(self,x):
        if self.__energy_level + x <=100:
            self.__energy_level += x
            return f"New energy level {self.__energy_level}"
        else:
            return "Energy level reaches the limit"
        

robot = Robot("Cr7")
robot.get_energy()
print(robot.set_energy(50))
print(robot.charge(40))
robot.get_energy()


# print(robot.__energy_level =  100)

robot.model()
robot._model = "ij33"
# robot.model()

