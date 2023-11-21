

class Student:
    """store student information"""
    def __init__(self, name, yearLevel, section):
        self.name = name
        self.yearLevel = yearLevel
        self.section = section

def addRecord():
    """add a student to the system"""
    try:
        print("\nFill up the student information")
        name = input("Enter full name: ").title()
        yearLevel = int(input("Enter year level: "))
        section = input("Enter section: ").upper()

        student = Student(name, yearLevel, section)

        with open("file_record.txt", "a") as f:
            f.write(f"{student.name} - {str(student.yearLevel)} - {student.section} \n")
        # The with statement ensures that the file is properly closed at the end of the block, regardless of any errors or exceptions that may occur.
        print("\nAdded successfully!")   
    except:
        print("INVALID INPUT!\n")

def viewRecord():
    """view all student record"""
    count = 0
    with open("file_record.txt", "r") as f:
        item = f.readlines()
        print("\n==== STUDENT RECORD ====")
        for student in item:
            count += 1
            print(f"{count}. {student.strip()}")
    if count == 0:
        print("Record is empty...\n")
    else:
        print(f"\n-----There are {count} student(s) in the record\n")

def editRecord():
    with open("file_record.txt", "r") as file:
        records = file.readlines()

    if len(records) == 0:
        print("\nRecord is empty...\nPlease input information before you can edit it.\n")
        return
    else:
        try:
            viewRecord()
            index = int(input("Enter the number you want to edit: ")) - 1

            with open("file_record.txt", "r") as file:
                records = file.readlines()

            if index >= 0 and index < len(records):
                record_item = records[index].strip().split(" - ")
                student = Student(record_item[0], record_item[1], record_item[2])

                print(f"\nSelected student: {student.name} - {student.yearLevel} - {student.section}")
                print("What do you want to change?")
                print("\t[1] Name")
                print("\t[2] Year Level")
                print("\t[3] Section")
                print("\t[4] All")
                choice = input("Enter your choice (1-4): ")

                if choice == "1":
                    new_name = input("Enter new name: ").title()
                    student.name = new_name
                    print("Name updated.", end="")
                elif choice == "2":
                    new_yearLevel = input("Enter new year level: ")
                    student.yearLevel = new_yearLevel
                    print("Year Level updated.", end="")
                elif choice == "3":
                    new_section = input("Enter new section: ").upper()
                    student.section = new_section
                    print("Section updated.", end="")
                elif choice == "4":
                    new_name = input("Enter new name: ").title()
                    new_yearLevel = input("Enter new year level: ")
                    new_section = input("Enter new section: ").upper()
                    student.name = new_name
                    student.yearLevel = new_yearLevel
                    student.section = new_section
                    print("All fields updated.", end="")
                else:
                    print("Invalid choice.")

                updated_record = f"{student.name} - {student.yearLevel} - {student.section}\n"
                records[index] = updated_record

                with open("file_record.txt", "w") as file:
                    file.writelines(records)

                print("SUCCESSFULLY UPDATED")
                modify_record("edit")
        except:
            print("Invalid index.")

def deleteRecord():
    with open("file_record.txt", "r") as file:
        records = file.readlines()

    if len(records) == 0:
        print("\nRecord is empty...\nPlease input information before you can edit it.\n")
        return
    else:
        viewRecord()
        index = int(input("Enter the number you want to delete: ")) - 1

        with open("file_record.txt", "r") as file:
            records = file.readlines()

        if index >= 0 and index < len(records):
            del records[index]

            with open("file_record.txt", "w") as file:
                file.writelines(records)
            print("SUCCESSFULLY DELETED")
            modify_record("delete")
        else:
            print("Invalid index.")

def modify_record(action):
    while True:
        again = input(f"\nDo you want to {action} another record? [Y/N]: ").lower()
        if again == "y":  
            if action == "add":
                addRecord()
            elif action == "edit":
                editRecord()
            elif action == "delete":
                deleteRecord()
            else:
                print("Invalid input. Please try again.")
                continue
        else:
            print("\n")
            break

def main():
    """main function to run the program"""
    while True:
        print("SYSTEM MENU:")
        print("[A] Add student")
        print("[E] Edit student")
        print("[V] View students")
        print("[D] Delete student")
        print("[X] Exit")
        userInput = input("Enter: ").upper()

        # Perform the selected operation
        if userInput == "A":
            addRecord()
            modify_record("add")
        elif userInput == "E":
            editRecord()
            
        elif userInput == "V":
            viewRecord()
        elif userInput == "D":
            deleteRecord()
        elif userInput == "X":
            break
        else:
            print("Invalid input, please try again.")

main()
