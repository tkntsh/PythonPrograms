#snack tracker python program using dictionaries and lists
snacks = ["chips", "candy", "soda", "cookies"]
prices = {"chips": 1.5, "candy": 0.75, "soda": 1.25, "cookies": 2.0}

print("My snacks:", snacks)
for snack in snacks:
    print(snack + " costs $" + str(prices[snack]))
