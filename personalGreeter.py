# personal_greeter.py
def greet(name, timeOfDay):
    print("Good " + timeOfDay + ", " + name + "!")

def addFavorite(num, fav):
    return num + fav

greet("Alex", "morning")
result = addFavorite(4, 8)
print("The result of your numbers added is: ", result)