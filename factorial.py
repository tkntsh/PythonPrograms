#Description: program accepts input from the user then calculates the factorial of that number 

print("Welcome. This program calculates the factorial of an integer you entered\n")

def factorial(x):
  if(x==1):
    return 1
  else:
    return x*factorial(x-1)

num = int(input("Enter an integer: "))
solution = factorial(num)
print(num, "! = ", solution)
