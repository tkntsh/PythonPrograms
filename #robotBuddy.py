#robot_buddy.py
class Robot:
    #defining robot characteristics
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery
    #defining robot funtion 1
    def sayHello(self):
        print(f"Beep boop! I'm {self.name}")
    #defining robot funtion 2
    def charge(self):
        self.battery += 20
        if self.battery > 100:
            self.battery = 100
        print(f"Batter after charge: {self.battery}%")
        
#create Robot instance
robo = Robot("Robocop", 100)
robo.sayHello()
robo.battery -= 30
print(f"Battery after work: {robo.battery}%")
robo.charge()