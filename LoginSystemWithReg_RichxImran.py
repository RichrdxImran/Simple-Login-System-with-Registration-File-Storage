#  Author: Al Imran Hossain
#  Date: January 24, 2024
#  Purpose: Simple login system with registration, login, and account viewing using file storage.

file_accounts = "accounts.txt"  # File for storing user accounts
current_user = None  # Tracks the currently logged-in user (None if no one is logged in)

def trim_input(user_input: str) -> str:
    """
    Removes leading and trailing spaces from user input.

    :param user_input: The input string from the user.
    :return: Cleaned string without leading or trailing spaces.
    """
    return user_input.strip()


def load_accounts() -> list:
    """
    Loads user accounts from the accounts file.

    :return: A list of user accounts as [username, password] pairs.
    """
    accounts = []
    try:
        with open(file_accounts, "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                accounts.append([username, password])
    except FileNotFoundError:
        pass  # If the file doesn't exist, return an empty list
    return accounts


def save_account(username: str, password: str):
    """
    Saves a new account to the file.

    :param username: The username of the new account.
    :param password: The password of the new account.
    """
    with open(file_accounts, "a") as file:
        file.write(f"{username},{password}\n")


def register():
    """
    Handles the user registration process.
    Checks for username availability and password length.
    """
    global current_user
    print("\nRegister New User")
    accounts = load_accounts()
    username = trim_input(input("Enter a username: "))
    password = trim_input(input("Enter a password (minimum 10 characters): "))

    # Check if password meets minimum length
    if len(password) < 10:
        print("Password too short! Please choose a password with at least 10 characters.")
        return

    # Check if the username is already taken
    for acc in accounts:
        if acc[0] == username:
            print("*Username already exists!* Please choose another username.")
            return

    save_account(username, password)
    print("User registered successfully!")


def login() -> bool:
    """
    Handles the user login process.
    If successful, sets the global current_user to the logged-in username.

    :return: True if login is successful, False otherwise.
    """
    global current_user
    if current_user:
        print(f"You are already logged in as: '{current_user}'.")
        return True

    print("\nLogin")
    username = trim_input(input("Enter username: "))
    password = trim_input(input("Enter password: "))
    accounts = load_accounts()

    # Check username and password match
    for acc in accounts:
        if acc[0] == username and acc[1] == password:
            current_user = username
            print("Logged in successfully!")
            return True

    print("Invalid username or password!")
    return False


def view_accounts():
    """
    Displays a list of all registered usernames.
    Requires the user to be logged in.
    """
    global current_user
    if not current_user:
        print("Please log in or register first.")
        return

    print("\nRegistered Accounts")
    accounts = load_accounts()
    for idx, acc in enumerate(accounts, start=1):  # Display account usernames only
        print(f"{idx}. {acc[0]}")


def menu():
    """
    Displays the main menu and handles user input to navigate through the system.
    """
    while True:
        print("\n*** MENU DASHBOARD ***")
        print("1. Register")
        print("2. Login")
        print("3. View Accounts")
        print("4. Exit")
        choice = trim_input(input("Choose an option (1, 2, 3, 4): "))

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            view_accounts()
        elif choice == "4":
            print("Exiting! Thank you for using the system.")
            break
        else:
            print("\n*Invalid option!* Please try again.")


if __name__ == "__main__":
    menu()