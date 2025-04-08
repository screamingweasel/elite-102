###################################################################################################
# Sample main python program to be tested
# Always structure your "main" as a function and then the only inline code should be 
# the call to main at the bottom. This is so your program can be imported as a module to call
# the functions without running the main code.
###################################################################################################
import sys

# Example function
def add_two(x,y):
    return x + y

def open_connection():
    return None

def add_account(first_name, last_name, email_address, pin, is_admin):
    # dummy for now
    return 1

def main():
    print("This is main.py")

# This is only true when the program is run from command line (not when imported)
if (__name__ == "__main__"):
    main()