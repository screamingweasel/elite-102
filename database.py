import mysql.connector

# Utility function to connect to MySql
def get_connection():
    connection = mysql.connector.connect(
        host='localhost', # << running on the same machine
        user = 'root',
        password='root', # << whatever you set during mysql config
        database='demo', # << your database name
        autocommit=True) # << save changes as soon as made
    return connection

def create_tables(conn):
    sql = "CREATE DATABASE IF NOT EXISTS demo"
    cursor = conn.cursor()
    cursor.execute(sql)

    sql = """
    CREATE TABLE IF NOT EXISTS demo.customers (
        customer_id INT NOT NULL AUTO_INCREMENT,
        customer_name VARCHAR(100),
        email_address VARCHAR(255),
        credit_limit DECIMAL(18,2),
    PRIMARY KEY (customer_id))
    """
    cursor.execute(sql)


def add_customer(conn, customer_name, email_address, credit_limit):
    # Demonstrates using placeholders for variable and passing data as a List
    sql = "INSERT INTO demo.customers (customer_name, email_address, credit_limit) values (%s, %s, %s)"
    data = [customer_name, email_address, credit_limit]
    cursor = conn.cursor()
    cursor.execute(sql, data)
    customer_id = cursor.lastrowid # << This returns auto_increment value of inserted row

    return customer_id


# Main Logic
def main():
    conn = get_connection()
    print("Connection opened")

    create_tables(conn)
    print("Table created")
    
    customer_id = add_customer(conn, 'Acme Fireworks', '123@demo.com', 10000)
    print(f"Inserted customer {customer_id}")

    customer_id = add_customer(conn, 'Zyzx Technologies', '456@demo.com', 12500)
    print(f"Inserted customer {customer_id}")
    
    customer_id = add_customer(conn, 'Bob''s Burgers', '789@demo.com', 7500)
    print(f"Inserted customer {customer_id}")

    conn.close()

# Best practice to put main logic in main() and call like this
if (__name__ == '__main__'):
    main()