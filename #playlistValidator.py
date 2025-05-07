#playlistValidator.py

#methods and defintions
#method to add song to playlist
def addSong(playlist):
    title = input("Enter the title of the song: ")
    
    while True:
        try:
            duration = float(input("Enter the durations of the song in minutes (eg: 3.5): "))
            
            if(duration<0):
                raise ValueError("Song duration must be positive")
            break
        except ValueError as e:
            print(f"Error: {e if str(e) else 'Please enter a valid number for the duration'}")
            
    while True:
        try:
            rating = float(input("Enter the rating of the song (eg: 1-5): "))
            
            if(not 1 <= rating <= 5):
                raise ValueError("The song rating must be between 1 and 5 (inclusive)")
            break
        except ValueError as e:
            print(f"Error: {e if str(e) else 'Please enter a valid number for the rating'}")
            
    #lists and dictionaries
    song = {"title": title, "duration": duration, "rating": rating}
    playlist.append(song)
    print(f"Added {title} ({duration} mins, {rating} stars)")

#method to view playlist    
def viewPlaylist(playlist):
    print("Playlist")
    for song in playlist:
        print(f"- {song['title']} ({song['duration']} mins, {song['rating']} stars)")
        
#method to save playlist to file
def savePlaylist(playlist):
    try:
        with open("playlist.txt", "w") as file:
            for song in playlist:
                file.write(f"{song['title']}, {song['duration']}, {song['rating']}\n")
        print("Saving playlist...")
    except IOError:
        print("Error: Could not save playlist to file!")
        
#main program/method
print("Welcome the Playlist Validator")
playlist = []

while True:
    print("Options: \n[1] Add a Song\n[2] View Playlist\n[3] Quit")
    choice = input("Enter your choice: ")
    
    if(choice == "1"):
        addSong(playlist)
        print("Debug playlist", playlist)
    elif(choice == "2"):
        viewPlaylist(playlist)
    elif(choice == "3"):
        savePlaylist(playlist)
        break
    else:
        print("Error: Invalid choice, try again.")
