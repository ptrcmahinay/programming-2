import time
import sys
import os

def start():
    print("+=========================+")
    print("|        MAIN MENU        |")
    print("+=========================+")
    print("| [A] Add Record          |")
    print("| [E] Edit Record         |")
    print("| [D] Delete Record       |")
    print("| [V] View Record         |")
    print("| [X] Exit Record         |")
    print("+=========================+")
    answer = input("Enter >> \u001b[34m").lower()
    sys.stdout.write("\033[0m")
    if answer == "a":
        add_record()
        modify_record("add")
        start()
    elif answer == "e":
        edit_record()
        modify_record("edit")
        start()
    elif answer == "d":
        delete_record()
        modify_record("delete")
        start()
    elif answer == "v":
        view_record()
        print("Do you want to")
        start()
    elif answer == "x":
        exit
    else: 
        print("Invalid input")
        start()

def modify_record(action):
    while True:
        again = input(f"Do you want to {action} another record? [Y/N]: ").lower()
        if again == "y":  
            if action == "add":
                add_record()
            elif action == "edit":
                edit_record()
            elif action == "delete":
                delete_record()
            else:
                print("Invalid input. Please try again.")
                continue
        else:
            print("\n")
            break
    

def add_record():
    print("\u001b[35m \n=== Add Record ===")
    sys.stdout.write("\033[0m")
    try:
        name = input(("Name: \u001b[34m \033[4m")).title()
        sys.stdout.write("\033[0m")

        section = input("section: \u001b[34m \033[4m")
        sys.stdout.write("\033[0m")

        yearLevel = input("Year Level: \u001b[34m \033[4m").upper()
        sys.stdout.write("\033[0m")
        print("\n")

    except ValueError:
        print("Invalid input.")
        add_record()
    else:
        for i in range(4):
            print("Adding record" + "."*i)
            sys.stdout.write("\033[F")
            time.sleep(1)
        sys.stdout.write("\033[F")
        print("Successfully added")
        num = len(record) + 1
        record[num] = (name, section, yearLevel)

def view_record():
    if not record:
        print("Record is empty.")
        start()
    else:
        print("{:<10} {:<30} {:<10} {:<10}".format('No.', 'NAME', 'section', 'yearLevel'))
        for key, value in record.items():
            name, section, yearLevel = value
            print("{:<10} {:<30} {:<10} {:<10}".format(key, name, section, yearLevel))

def edit_record():
    print("\n=== Edit Record ===")
    view_record()
    try:
        edit_record = int(input("What number do you want to edit? "))
    except:
        print("Please enter a number")
        edit_record()
    else:
        if edit_record in record:
            for key, value in record.items():
                if key == edit_record:
                    change = input(("what do you want to change?[Name, section, yearLevel]? ")).lower()
                    if change == "name":
                        new_name = input("Enter new name: ").title()
                        record[key] = (new_name, value[1], value[2])
                    elif change == "section":
                        new_section = input("Enter new section: ")
                        record[key] = (value[0], new_section, value[2])
                    elif change == "yearLevel":
                        new_yearLevel = (input("Enter new yearLevel: "))
                        record[key] = (value[0], value[1], new_yearLevel,)
                    print("Here's the updated record")
                    view_record()

def delete_record():
    print("\n=== Delete Record ===")
    view_record()
    try:
        delete_record = int(input("What number do you want to delete? "))
    except:
        print("Please enter a number")
        delete_record()
    else:
        if delete_record in record:
            del record[delete_record]
            print(f"Record {delete_record} has been deleted.")
            view_record()
        else:
            print("Invalid record number")

record = {}
start()
