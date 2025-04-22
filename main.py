import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host='localhost', # << running on the same machine
        user = 'root',
        password='root', # << whatever you set during mysql config
        database='demo', # << your database name
        autocommit=True) # << save changes as soon as made
    return connection

def edit_customer(customer_id):
    customer_name = input("Customer Name: ")
    credit_limit = int(input("Credit Limit: "))
    print("If this were implemented we would update the following")
    print(f"{customer_name=}")
    print(f"{credit_limit=}")

def insert_users(user_name,email_address,admin_flag,password):
    sql = """
    INSERT INTO `bank`.`users`
    (`user_name`,
    `email_address`,
    `admin_flag`,
    `password`)
    VALUES (%s,%s,%s,%s)
    """
    data = [user_name, email_address, admin_flag, password]
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(sql, data)
    id = cursor.lastrowid # << This returns auto_increment value of inserted row
    return id

def create_user():
    user_name = input("Name: ")
    email_address = input("Email Address: ")
    password = input("Password: ")
    admin_flag = False

    id = insert_users(user_name,email_address,admin_flag,password)
    print("Account Created")
    return id

"""
INSERT INTO `bank`.`accounts`
(`user_id`,
`balance`,
`active_flag`,
`accountscol`)
VALUES (%s,%s,%s,%s);
"""

def create_customer():
    # Make sure that this is a new email address
    while True:
        email_address = input("Email Address: ")
        if (get_customer_by_email(email_address) is not None):
            print("That email is unavailable")
            continue
        else:
            break
        
    customer_name = input("Customer Name: ")
    credit_limit = int(input("Credit Limit: "))

    customer = add_customer(customer_name, email_address, credit_limit)
    input("Customer added. Press Enter to continue")


def get_customer_by_email(email_address):
    sql = "SELECT * FROM demo.customers where email_address = %s"
    data = [email_address]
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(sql, data)
    return cursor.fetchone()


def add_customer(customer_name, email_address, credit_limit):
    # Demonstrates using placeholders for variable and passing data as a List
    sql = "INSERT INTO demo.customers (customer_name, email_address, credit_limit) values (%s, %s, %s)"
    data = [customer_name, email_address, credit_limit]
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(sql, data)
    customer_id = cursor.lastrowid # << This returns auto_increment value of inserted row
    return customer_id

def make_deposit():
    amt = input("Enter Deposit Amount: ")
    print(amt)
    return

def handle_choice(choice):
    pass

def show_main_menu():
    print("Menu:")
    print("1. Create new customer")
    print("2. Edit Customer")
    print("3. Delete Customer")
    print("4. Make Deposit")
    print("x. Exit")

def login():
    email_address = input("Email Address: ")
    password = input("Enter Password: ")
    customer = get_customer_by_email(email_address)
    print(customer)
    return None

def main():
    customer_id = login()
    if customer_id is None:
        add_account = input("Would you like to open an account")
        if add_account == 'y':
            customer_id = create_user()
        else:
            print("Goodbye.")
            return

    while True:
        show_main_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            create_user()
        elif choice == '2':
            print("Executing Option 2...")
            edit_customer(1) # Need a customer #!!!
        elif choice == '2':
            print("Executing Option 3...")
        elif choice == '4':
            make_deposit()
        elif choice.lower() == 'x':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if (__name__ == '__main__'):
    main()
