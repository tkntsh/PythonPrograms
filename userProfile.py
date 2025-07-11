# user_profile.py
import json

def collect_profile():
    try:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        hobby = input("Enter favorite hobby: ")
        return {"name": name, "age": age, "hobby": hobby}
    except ValueError:
        print("Error: Age must be a number.")
        return None

def save_profile(profile, filename="user_profile.json"):
    try:
        # Read existing profiles or initialize empty list
        try:
            with open(filename, 'r') as file:
                profiles = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            profiles = []

        # Add new profile
        profiles.append(profile)
        
        # Save to JSON file
        with open(filename, 'w') as file:
            json.dump(profiles, file, indent=4)
        print(f"Profile saved to {filename}")
    except Exception as e:
        print(f"Error saving profile: {e}")

def read_profiles(filename="user_profile.json"):
    try:
        with open(filename, 'r') as file:
            profiles = json.load(file)
            for i, profile in enumerate(profiles, 1):
                print(f"\nProfile {i}:")
                print(f"Name: {profile['name']}")
                print(f"Age: {profile['age']}")
                print(f"Hobby: {profile['hobby']}")
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in file.")
    except Exception as e:
        print(f"Error reading profiles: {e}")

def main():
    print("User Profile Manager")
    while True:
        profile = collect_profile()
        if profile:
            save_profile(profile)
        choice = input("\nAdd another profile? (y/n): ").lower()
        if choice != 'y':
            break
    print("\nDisplaying all profiles:")
    read_profiles()

if __name__ == "__main__":
    main()