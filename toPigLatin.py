#Author: Ntshangase Ntokozo
#St: 4123601
#Description: Program that accepts a word from the user to change the word to pig-latin

print("Welcome. This program accepts input from the user and changes the string entered to pig-latin")

word = input("Please enter a word to be changed: ")
letter = word[0]
word2 = ""
num = len(word)

if(word[0].upper() != "A" or "E" or "I" or "O" or "U"):
    word2 = word[1:num] + letter + "yay"
    print("The translation to pig-latin of the word: ", word, " is ", word2)
elif(word[0] == "A" or "E" or "I" or "O" or "U"):
    word2 = word + "yay"
    print("The translation to pig-latin of the word: ", word, " is ", word2)