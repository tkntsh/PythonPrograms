# robotBuddy.py
class Robot:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery
    
    def say_hello(self):
        print(f"Beep boop! I’m {self.name}!")
    
    def charge(self):
        self.battery += 20
        # cap battery at 100%
        if self.battery > 100:
            self.battery = 100
        print(f"Battery after charging: {self.battery}%")

# creating a robot object and test it
my_robot = Robot("Zoomer", 100)
my_robot.say_hello()
# simulating batter drain
my_robot.battery -= 30 
print(f"Battery after work: {my_robot.battery}%")
my_robot.charge()
