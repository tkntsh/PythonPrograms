#Author: Ntshangase Ntokozo
#St: 4123601
#Description: Program that accepts two numbers from the user and does calculations with it

print("Welcome. This program accepts two integers from the user to do calculations")

def Add(x,y):
    res = x+y
    print(res)

def Sub(x,y):
    res = x-y
    print(res)

def Mul(x,y):
    res = x*y
    print(res)

def Div(x,y):
    res = x%y
    print(res)

num1 = int(input("Please enter your first integer: "))
num2 = int(input("Please enter your second integer: "))
operation = input("Please enter what operation you would like to be executed: ")

if(operation == "+"):
    print("The sum of ",num1, " and ",num2, " is equal to ", Add(num1,num2))
elif(operation == "-"):
    print("The difference of ",num1, " and ",num2, " is equal to ", Sub(num1,num2))
elif(operation == "*"):
    print("The product of ",num1, " and ",num2, " is equal to ", Mul(num1,num2))
elif(operation == "%"):
    print("The quotiant of ",num1, " and ",num2, " is equal to ", Div(num1,num2))
else:
    print("Error: Enter a valid operation")