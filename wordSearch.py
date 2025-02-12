#Description: Program that accepts a word from the user to mirror it

print("Welcome. This program accepts input of two words to check if these words are the same or have the same elements")

minWord = ""
count = 0

word = input("Please enter a word: ")
sort = input("Please enter a word to search for: ")

for x in range(len(word)):
    minWord = minWord + word[x]
    if(sort in minWord):
        count += 1
        minWord = ""

if(count>1):
    print("There are {0} {2}s in the string '{1}'".format(count,word,sort))
else:
    print("There is {0} {2} in the string '{1}'".format(count,word,sort))
