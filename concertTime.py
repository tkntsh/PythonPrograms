#concertTime.py
import myTool
import random
import datetime

#random concert seating
luckNum = random.randint(1, 100)
print("Your seat for the concert is: Seat", luckNum)

#date and time of concert
concertDateTime = datetime.datetime.now()
print("Concert time:", concertDateTime, "Enjoy the show!")

#use custom module and user input
performingArtistName = input("Whose concert would you like to attend? ")
message = myTool.cheer(performingArtistName)
print(message)
