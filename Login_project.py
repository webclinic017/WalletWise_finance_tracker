# importing Operations file
import Operations

# importing Identity class from Operations file
from Operations import Identity

# importing file calc_test
import main_program

import sendmail

# opening a loop for login operations
Open = ""

while Open == "":

    # creating and exception for the value error
    while True:

        try:
            Open = input('''Enter 0 to sign-up:\nEnter 1 to login : ''')
            if Open != "1" and Open != "0":
                raise ValueError
            break

        except ValueError:
            print("Invalid input, the system expects a 0 or 1")

    # calling username list
    Username_List = Identity.username_list()
    if Open == "0":
        username = input("Enter a Username: ")
        while username == "":
            print("Username cannot be empty")
            username = input("Try Again: ")
            Open = ""
            # break
        # checking if user's chosen username isn't already existing
        for user in Username_List:
            while user == username:
                username = input("Username Exists, Try Again: ")
                Open = ""

        # creating a password
        password = Operations.Check_password()

        # registering an email
        global email_address

        email_address = Operations.Check_email()

        # recording user's username, password, and email
        Identity.sign_up(username, password, email_address)

        # Welcoming the new registered user
        sendmail.sendemail(email_address)
        print(f"Welcome to wallet wise, {username}")

        # creating expenses and income sheets for the new user in the workbook
        Identity.new_excel_sheet(username)

        # creating an exception for value error
        while True:
            try:
                response = input("""Would you like to continue with transactions now?
                            Enter 1 to continue
                            Enter 0 to exit \n""")
                if response != "1" and response != "0":
                    raise ValueError
                break

            except ValueError:
                print("Invalid input, the system expects a 0 or 1")

        if response == "1":
            Open = ""

        elif response == "0":
            print(
                f'''Thanks for registering with the wallet wise {username}! \nHere's to making better financial decisions. Good bye :)''')
            # sendmail.EmailMessage(email_address)
            exit()


    elif Open == "1":
        login_username = input("Enter your username: ")

        # checking if the username is registered
        while login_username not in Username_List:
            print("Username doesn't exist")

            # creating a variable for users to try again if the first input was incorrect
            try_again = input("Enter 1 to retry or 0 to exit: ")

            if try_again == "1":
                login_username = input("Enter Your Username: ")

            if try_again == "0":
                break


        # checking if the user's input details match
        else:
            no = Username_List.index(login_username)
            password = input("Enter a Password: ")
            feedback = Identity.user_matrix(login_username, password, no)

            # calling a method to access user's info
            if feedback == True:
                main_program.mainProgram(login_username)