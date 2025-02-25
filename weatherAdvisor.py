#weather advisory python progam
temp = float(input("What’s the temperature? "))

if temp < 10:
    print("Wear a jacket!")
elif temp <= 20:
    print("A sweater should do.")
else:
    print("T-shirt weather!")
