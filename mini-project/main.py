import json
import os

FILENAME = "passwords.json"


def load_passwords():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)  # {}
    return {}


def save_password(data):
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)


def add_password():
    website = input("Enter website name ===>>> ").strip()
    username = input(f"Enter your {website} username ===>>> ").strip()
    password = input(f"Enter password for {username} ===>>> ").strip()

    data = load_passwords()
    data[website] = {"username": username, "password": password}

    save_password(data)
    print("✅ Password saved successfully !! ")

def view_password():
    website = input("Enter your website name ==>>> ").strip()
    data = load_passwords()
    
    if website in data:
        print("\n")
        print(f"🌐 Website :- {website}")
        print(f"🙎🏻‍♂️ Username :- {data[website]['username']}")
        print(f"🔐 Password :- {data.get(website).get('password')}")
    else:
        print(f"❌ No entry found for this website")

def show_all_passwords():
    data = load_passwords()
    if not data:
        print("❌ No password founds")
        return
    
    print("All sved passwords")
    
    for website, info in data.items():
        print(f"- {website}: {info['username']} / {info['password']}")
        
def menu():
    while True:
        print("\n 🔐 Welcome to Password Manger ")
        print("1. Add new Password")
        print("2. View a Password")
        print("3. Show all passwords")
        print("4. Exit")

        choice = input("Choose an option 1-4 :---->> ").strip()

        if choice == "1":
            add_password()
        elif choice == "2":
            view_password()
        elif choice == "3":
            show_all_passwords()
        elif choice == "4":
            print(" 👋🏼 Goodbye ")
            break
        else:
            print("❌ Invalid choice. Please Try Again")


menu()
