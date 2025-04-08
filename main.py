# "simple command line menu in python"

def show_menu(options):
    print("Menu:")
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")

def get_choice(options):
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    options = ["Option 1", "Option 2", "Option 3", "Exit"]
    while True:
        show_menu(options)
        choice = get_choice(options)

        if choice == len(options):
            break
        else:
            print(f"You chose: {options[choice - 1]}")

if __name__ == "__main__":
    main()