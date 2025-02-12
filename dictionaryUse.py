#Description: Program that accepts input from the user to create purchase order using dictionary

print("Welcome. This program creates a purchase list from input you have entered. Also displays the most expensive item and the average of the prices entered \n")

def printOut(order):
  if(len(order)<1):
    print("Error: No items were entered")
  else:
    print(order)

def avg(order):
    avgPrice = {}
    for k,v in orders.iteritems():
        # v is the list of prices for items entered k
        avgPrice[k] = sum(v)/ float(len(v))
        print("Average price for items entered is: R", avgPrice)

def mostExpensive(order):
    order.sort()
    print("Largest element is :", order[-1])

orders = {}
userIn = ""

while True:
  userIn = input("Do you want to enter an item(s) [y/n]: ")

  if(userIn.lower()=="n"):
    printOut(orders)
    break
  
  item =  input("Enter an item: ")
  price = input("Enter the price of item: ")

  orders[item] = price
  printOut(orders)
  avg(orders)
