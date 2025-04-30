#musicCollection.py
import random
import datetime

#Song class (OOP)
class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
        #time song is added
        self.addedTime = datetime.datetime.now()
    
    def play(self):
        return f"Now playing: {self.title} by {self.artist} for {self.duration} minutes!"

#Artist class (OOP)
class Artist:
    def __init__(self, name):
        self.name = name
        #dictionary: albumName = list of songs
        self.albums = {}
    
    def addSong(self, song, album="Single"):
        if album not in self.albums:
            self.albums[album] = []
        self.albums[album].append(song)

#function to add a song
def addSong(collection):
    #input
    title = input("Song title: ") 
    artistName = input("Artist name: ")
    #variable handling
    duration = float(input("Duration (in minutes, e.g., 3.5): "))
    if artistName not in collection:
        collection[artistName] = Artist(artistName)
    collection[artistName].addSong(Song(title, artistName, duration))
    #String formatting
    print(f"Added {title} by {artistName} at {datetime.datetime.now()}")

#function to view collection
def viewCollection(collection):
    print("Your Collection:")
    for artistName, artist in collection.items():
        #string manipulation
        print(f"Artist: {artistName.upper()}")
        for album, songs in artist.albums.items():
            print(f"  Album: {album}")
            #loop statements
            for song in songs:
                print(f"    - {song.title} ({song.duration} mins)")

#function to save collection (file handling)
def saveCollection(collection):
    with open("musicCollection.txt", "w") as file:
        for artistName, artist in collection.items():
            for album, songs in artist.albums.items():
                for song in songs:
                    file.write(f"{song.title},{song.artist},{song.duration},{song.addedTime}\n")
    print("Saving collection to musicCollection.txt...")

#function to load collection (file handling)
def loadCollection():
    collection = {}
    try:
        with open("musicCollection.txt", "r") as file:
            for line in file:
                title, artist, duration, timestamp = line.strip().split(",")
                if artist not in collection:
                    collection[artist] = Artist(artist)
                collection[artist].addSong(Song(title, artist, float(duration)))
        print("Loaded collection from file!")
    except FileNotFoundError:
        print("No previous collection found, starting fresh.")
    return collection

#main program
print("Welcome to Music Collection Manager!")
#operators
collection = loadCollection() 
#loops
while True: 
    print("Options: [1] Add Song, [2] View Collection, [3] Play Song, [4] Random Pick, [5] Quit")
    choice = input("Choice: ")
    #conditionals
    if choice == "1": 
        addSong(collection)
    elif choice == "2":
        viewCollection(collection)
    elif choice == "3":
        title = input("Enter song title to play: ")
        found = False
        for artist in collection.values():
            for album in artist.albums.values():
                for song in album:
                    #String comparison
                    if song.title.lower() == title.lower():
                        print(song.play())
                        found = True
                        break
        if not found:
            print("Song not found!")
    elif choice == "4":
        allSongs = [song for artist in collection.values() for album in artist.albums.values() for song in album]
        if allSongs:
            #modules
            random_song = random.choice(allSongs)
            print(f"Random pick: {random_song.play()}")
        else:
            print("No songs in collection yet!")
    elif choice == "5":
        saveCollection(collection)
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again!")