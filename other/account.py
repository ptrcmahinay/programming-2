#Account authentication using list

class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def account():
    usernames = ["Aslie", "Patricia"]
    password = ["0110", "1022"]

    u_input = input("Username: ").title()
    p_input = input("Password: ")

    account_found = False

    for i in range(len(usernames)):
        if u_input == usernames[i] and p_input == password[i]:
            account_found = True
            print(f"Welcome {u_input}")
            break

    if not account_found:
        print("Account not found or wrong password")