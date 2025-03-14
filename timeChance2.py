# timeChance2.py
import random
import datetime
import my_tools

# Random lucky number
lucky_number = random.randint(1, 100)
print("Your lucky number is:", lucky_number)

# Current date and time
current_time = datetime.datetime.now()
print("Current time:", current_time, "- Time to shine!")

# Use custom module with name and lucky number
name = input("What’s your name? ")
message = my_tools.cheer(name, lucky_number)
print(message)
