# This is my first mini project in Python after learning the basics of Python programming.
# The project is a simple personal journal application that allows users to create, read, update, and delete journal entries.
# The entries are stored in a text file with date on it.

import datetime
import os

try:
    base_dir = os.path.dirname(os.path.abspath(__file__))
except NameError:
    base_dir = os.getcwd()
journal_file = os.path.join(base_dir, "journal.txt")

while True:
    print("Welcome to your personal journal!"
          "\nPlease choose an option:"
          "\n1. Create a new entry"
          "\n2. Read existing entries"
          "\n3. Update an existing entry"
          "\n4. Delete an existing entry"
          "\n5. Exit"
            )
    input_choice = input("Enter your choice (1-5): ")
    if input_choice == "1":
        with open(journal_file, "a", encoding="utf-8") as file:
            entry = input("Enter your journal entry: ")
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"[{date}] {entry}\n")
        
    elif input_choice == "2":
        if not os.path.exists(journal_file):
            print("No entries found.")
        else:
            with open(journal_file, "r", encoding="utf-8") as file:
                entries = file.readlines()
            if len(entries) == 0:
                print("No entries found.")
            else:
                for entry in entries:
                    print(entry.strip())
        
    elif input_choice == "3":
        if not os.path.exists(journal_file):
            print("No entries found.")
        else:
            with open(journal_file, "r", encoding="utf-8") as file:
                entries = file.readlines()
            if len(entries) == 0:
                print("No entries found.")
            else:
                for i, entry in enumerate(entries):
                    print(f"{i + 1}. {entry.strip()}")
                try:
                    entry_number = int(input("Enter the number of the entry you want to update: "))
                except ValueError:
                    print("Invalid input. Please enter a number.")
                else:
                    if entry_number < 1 or entry_number > len(entries):
                        print("Invalid entry number.")
                    else:
                        new_entry = input("Enter the updated journal entry: ")
                        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        entries[entry_number - 1] = f"[{date}] {new_entry}\n"
                        with open(journal_file, "w", encoding="utf-8") as file:
                            file.writelines(entries)
                        print("Entry updated successfully.")
        
    elif input_choice == "4":
        if not os.path.exists(journal_file):
            print("No entries found.")
        else:
            with open(journal_file, "r", encoding="utf-8") as file:
                entries = file.readlines()
            if len(entries) == 0:
                print("No entries found.")
            else:
                for i, entry in enumerate(entries):
                    print(f"{i + 1}. {entry.strip()}")
                try:
                    entry_number = int(input("Enter the number of the entry you want to delete: "))
                except ValueError:
                    print("Invalid input. Please enter a number.")
                else:
                    if entry_number < 1 or entry_number > len(entries):
                        print("Invalid entry number.")
                    else:
                        del entries[entry_number - 1]
                        with open(journal_file, "w", encoding="utf-8") as file:
                            file.writelines(entries)
                        print("Entry deleted successfully.")
        
    elif input_choice == "5":
        print("Thank you for using your personal journal!")
        break
exit()
