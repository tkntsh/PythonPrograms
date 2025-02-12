#Ntokozo Ntshangase
#St! 4123601
#Description: Program that accepts input from the user to create and and two matrix

print("Welcome. This program creates and adds two matrix from input you have entered\n")

def printOut(matrix):
    if(len(x)<1):
        print("Error: There are no items entered in this x matrix")
    elif(len(y)<1):
        print("Error: There are no items entered in this y matrix")
    else:
        print(x, "\t", y)

x = []
y = []
result = []
userIn = ""

for i in range(len(x)<4):
    userX = input("Enter an integer to add to the first matrix: ")
    x.add(userX)
    for j in range(len(y)<4):
        userY = input("Enter an integer to add to the second matrix: ")
        y.add(userY)
        result[i][j] = x[i][j] + y[i][j]

print(result)