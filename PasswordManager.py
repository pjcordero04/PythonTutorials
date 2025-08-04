user_credentials = {}

def run_login():
    while True:
        mode = input("\nType what you want to do ('register', 'login', 'change password', 'quit'): ").lower()

        if mode == "register":
            username = input("Enter a username: ")
            if username in user_credentials:
                print("Username already exists.")
            else:
                password = input("Enter a password: ")
                user_credentials[username] = password
                print("Registration successful!")

        elif mode == "login":
            login_user = input("Enter your username: ")
            login_pass = input("Enter your password: ")

            if login_user in user_credentials and user_credentials[login_user] == login_pass:
                print(f"\nWelcome, {login_user}! You are now logged in.")

                # Logged-in menu
                while True:
                    sub_mode = input("\nChoose an option ('logout', 'change password', 'quit'): ").lower()

                    if sub_mode == "logout":
                        print("You have been logged out.")
                        break  # Exit the sub-menu

                    elif sub_mode == "change password":
                        current_pass = input("Enter your current password: ")
                        if user_credentials[login_user] == current_pass:
                            new_pass = input("Enter your new password: ")
                            user_credentials[login_user] = new_pass
                            print("Password changed successfully!")
                        else:
                            print("Incorrect current password.")

                    elif sub_mode == "quit":
                        print("Exiting the program. Goodbye!")
                        return  # Exits the whole function

                    else:
                        print("Invalid option. Try again.")

            else:
                print("Invalid username or password.")

        elif mode == "change password":
            login_user = input("Enter your username: ")
            login_pass = input("Enter your old password: ")
            if login_user in user_credentials and user_credentials[login_user] == login_pass:
                new_pass = input("Enter your new password: ")
                user_credentials[login_user] = new_pass
                print("You have changed your password successfully!")
            else:
                print("Invalid username or password.")

        elif mode == "quit":
            print("Program ended.")
            break

        else:
            print("Invalid mode input. Please try again.")

run_login()
