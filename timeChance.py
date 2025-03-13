# timeChance.py
import random
import datetime
import my_tools

# Step 1: Random lucky number
lucky_number = random.randint(1, 100)
print("Your lucky number is:", lucky_number)

# Step 2: Current date and time
current_time = datetime.datetime.now()
print("Current time:", current_time, "- Time to shine!")

# Step 3 & 4: Use custom module with user input
name = input("What’s your name? ")
message = my_tools.cheer(name)
print(message)
