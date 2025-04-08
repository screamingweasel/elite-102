def show_main_menu():
    print("Menu:")
    print("1.Create new customer")
    print("2. Edit Customer")
    print("3. Delete Customer")
    print("x. Exit")

def edit_customer(customer_id):
    customer_name = input("Customer Name: ")
    credit_limit = int(input("Credit Limit: "))
    print("If this were implemented we would update the following")
    print(f"{customer_name=}")
    print(f"{credit_limit=}")

    # TODO: update logic goes here

    return

def handle_choice(choice):
    if choice == '1':
        print("Executing Option 1...")
    elif choice == '2':
        print("Executing Option 2...")
        edit_customer(1) # Need a customer #!!!
    elif choice == '2':
        print("Executing Option 3...")
    elif choice.lower() == 'x':
        print("Exiting...")
        return True
    else:
        print("Invalid choice. Please try again.")
    return False

def main():
    while True:
        show_main_menu()
        choice = input("Enter your choice: ")
        if handle_choice(choice):
            break

if (__name__ == '__main__'):
    main()
