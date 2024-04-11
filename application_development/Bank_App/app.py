def main_menu():
    print("Welcome to the Main Menu")
    print("1. Login")
    print("2. Signin")
    print("3. Exit")


def get_user_choice():
    choice = input("Please enter your choice: ")
    return choice


def user_menu(username):
    print("welcome " + username)
    print("a. Amount Deposit")
    print("b. Amount Withdrawal")
    print("c. Check Balance")
    print("d.Exit")


def main():
    while True:
        main_menu()
        choice = get_user_choice()

        if choice == '1':
            username = input("enter username")
            password = input("enter password")
            if username == "aswin" and password == "2002":
                user_menu(username)
                choice = get_user_choice()
                if choice == 'a':
                    amount = input("enter amount to deposit")
                    print("amount deposited successfully")
                elif choice == 'b':
                    withdraw_amount = input("enter withrawl amount")
                    print("amount withdrawn successfully")
                elif choice == 'c':
                    print("balance is 200")
        elif choice == '2':
            print("You selected Option 2")
            # Do something for Option 2
        elif choice == '3':
            print("You selected Option 3")
            # Do something for Option 3
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
