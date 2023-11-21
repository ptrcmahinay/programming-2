#Account authentication using dictionary

import json
accounts = {
    "gcash": ("patricia", "0123"),
    "fb": ("ptrcmahinay@gmail.com", "hello"),
    "school gmail": ("patricia.mahinay@evsu.edu.ph", "EVSUcutie")
}

def addNewAccount():
    """Add new account"""
    app = input("app: ")
    u_input = input("Username:")
    u_pass = input("Password:")
    
    accounts[app] = (u_input, u_pass)

    with open("other/accounts.json", "w") as file_account:
        json.dump(accounts, file_account, indent=4)
        # json.dump = python string to json object

def accountSearch():
    """Search for accounts in a JSON file"""
    app = input("App: ")

    with open("other/accounts.json", "r") as file:
        accounts = json.load(file)
        # json.load - json string to python object

    account_found = False
    for key, value in accounts.items():
        username, password = value
        if key == app:
            print(f"Username: {username}\nPassword: {password}")
            account_found = True
            break
    
    if not account_found:
        print("App not found")

# def confirmation():
#     with open("other/credentials.txt", "r") as file:
#             stored_credentials = file.readline().strip().split(" - ")

#     stored_username = stored_credentials[0]
#     stored_password = stored_credentials[1]

#     # Prompt the user to enter their username and password
#     entered_username = input("Enter your username: ")
#     entered_password = input("Enter your password: ")

#     # Check if the entered credentials match the stored credentials
#     if entered_username == stored_username and entered_password == stored_password:
#         print("Login successful. You can now access your accounts.")
#         print("Login successful. Identity confirmed.")
#         print(f"Login successful. Welcome {entered_username}")
#         do = input("Do you want to add a new account [A] or search for accounts? [S]: ").upper()
#         if do == 'A':
#             addNewAccount()
#         elif do == 'S':
#             accountSearch()
#         else:
#             print("Invalid input")
#     else:
#         print("Login failed, please try again")

# confirmation()

do = input("Do you want to add a new account [A] or search for accounts? [S]: ").upper()
if do == 'A':
    addNewAccount()
elif do == 'S':
    accountSearch()
else:
    print("Invalid input")

