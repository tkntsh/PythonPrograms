print("Welcome this program asks for your name\n")

name = input("Please enter your name or Quit to exit: ")
while(name.upper()!="QUIT"):
    print("Welcome ", name)
    name = input("Please enter your name or Quit to exit: ")

print("Thank you")