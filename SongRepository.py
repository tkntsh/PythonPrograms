# songrepository.py
song1 = input("What song do you want to save: ")

# w = write
with open("songList.txt", "w") as file:
    file.write(song1 + "\n")
print("Saved to Playlist!")

# r = read
with open("songList.txt", "r") as file:
    fileContent = file.read()
print("Song(s) on playlist: ", fileContent)

# a = add/append
song1 = input("Add another song: ")
with open("songList.txt", "a") as file:
    file.write(song1 + "\n")

# r = display
with open("songList.txt", "r") as file:
    fullFileContent = file.read()
print("Song(s) from Playlist: ", fullFileContent)