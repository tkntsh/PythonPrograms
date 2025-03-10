# fileHandling.py
message1 = input("Input your favourite song: ")

# w = write first message
with open("memory.txt", "w") as file:
    file.write(message1 + "\n")
print("Message saved.")

# r = read/display
with open("memory.txt", "r") as file:
    fileContent = file.read()
    print("From the vault: " + fileContent)

# a = append
message2 = input("Add another song: ")
with open("memory.txt", "a") as file:
    file.write(message2 + "\n")
print("Updated file saved.")

# displaying full file content
with open("memory.txt", "r") as file:
    fullContent = file.read()
    print("From the vault: " + fullContent.strip())