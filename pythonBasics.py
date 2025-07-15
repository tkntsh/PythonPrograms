#python basics

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} is barking!")
        
    def breedType(self):
        print(f"Breed of type: {self.breed}!")
        
name = input("Enter your dog's name: ")
breed = input("Enter the breed of your dog: ")
dog = Dog(name, breed)
dog.bark()
dog.breedType()