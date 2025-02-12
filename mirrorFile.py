#Author: Ntshangase Ntokozo
#St: 4123601
#Description: Program that accepts a word from the user to mirror it

print("Welcome. This program accepts input from the user to mirror the word")

word = input("Please enter a word: ")
mirror = ""

for c in range (len(word)-1,-1,-1):
    mirror += word[c]

print("Mirror image of the word {0} is {1} when you combine the words you get {2}".format(word,mirror, word+mirror))
