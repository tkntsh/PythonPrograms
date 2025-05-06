#playlistValidator.py
def add_song(playlist):
    #input
    title = input("Enter song title: ")
    while True:
        #try and catch
        try:
            #variables
            duration = float(input("Enter duration (in minutes, e.g., 3.5): "))  # Variables - Lesson 2
            if duration <= 0:
                raise ValueError("Duration must be positive.")
            break
        except ValueError as e:
            print(f"Error: {e if str(e) else 'Please enter a valid number for duration.'}")
    
    while True:
        #try and catch
        try:
            rating = int(input("Enter rating (1-5): "))
            if not 1 <= rating <= 5:
                raise ValueError("Rating must be between 1 and 5.")
            break
        except ValueError as e:
            print(f"Error: {e if str(e) else 'Please enter a valid integer.'}")
    #lists & dictionary
    song = {"title": title, "duration": duration, "rating": rating}
    playlist.append(song)
    print(f"Added {title} ({duration} mins, {rating} stars)")

def view_playlist(playlist):
    print("Playlist:")
    for song in playlist:
        print(f"- {song['title']} ({song['duration']} mins, {song['rating']} stars)")
#method for file handling
def save_playlist(playlist):
    try:
        with open("playlist.txt", "w") as file:
            for song in playlist:
                file.write(f"{song['title']},{song['duration']},{song['rating']}\n")
        print("Saving playlist...")
    except IOError:
        print("Error: Could not save playlist to file.")

#main program
print("Welcome to Music Playlist Validator!")
#bug: if you use 'playlst' later, it will fail
playlist = []

while True:
    print("Options: [1] Add Song, [2] View Playlist, [3] Quit")
    choice = input("Choice: ")
    
    if choice == "1":
        add_song(playlist)
        #debugging with print
        print("Debug: Playlist now:", playlist)  
    elif choice == "2":
        #bug: try 'playlst' here to see NameError
        view_playlist(playlist)
    elif choice == "3":
        save_playlist(playlist)
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again!")