def show_menu():
    print("Menu:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Exit")

def handle_choice(choice):
    if choice == '1':
        print("Executing Option 1...")
    elif choice == '2':
        print("Executing Option 2...")
    elif choice == '3':
        print("Exiting...")
        return True
    else:
        print("Invalid choice. Please try again.")
    return False

while True:
    show_menu()
    choice = input("Enter your choice: ")
    if handle_choice(choice):
        break
