import string 
import random
def show_menu():
    print("------ PASSWORD MANAGER ------")
    print("1. Add Password")
    print("2. View Accounts")
    print("3. Search Password")
    print("4. View Password")
    print("5. Update Password")
    print("6. Delete Password")
    print("7. Generate Password")
    print("8. Exit")

def create_master_password():
    try:
        with open("master.txt", "r") as file:
            master = file.read().strip()
            if master != "":
                return   
    except FileNotFoundError:
        pass
    print("No master password found!")
    while True:
        new_master = input("Create a new master password: ").strip()
        if new_master == "":
            print("Master password cannot be empty or only spaces. Try again!\n")
        else:
            break
    with open("master.txt", "w") as file:
        file.write(new_master)
    print("Master password created successfully!\n")

def login():
    try:
        with open("master.txt", "r") as file:
            master = file.read().strip()
    except FileNotFoundError:
        print("Master password file missing!")
        return False
    attempt=0
    while attempt>0:
        entered=input("enter the master password")
        if master==entered:
            print("Access Grant Successfully \n")
            return True
        attempt-=1
        print("Wrong Password")
    print("Too many wrong password")
    return False
def password_generator():
    length=int(input("Enter Password length (reccomended= 8-14 Letters)"))
    if length<8:
        print("Password too short! Use at least 6 characters.\n")
        return None
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    print(f"Generated Password: {password}\n")
    return password

def dup_accprevention(searched):
    try:
        with open("password.txt", "r") as file:
            lines = file.readlines()
        if not lines:
            return 1
        for line in lines:
            account = line.split("|")[0].strip()
            if account == searched:
                return 0  
        return 1  
    except FileNotFoundError:
        return 1  

def add_password():
    account = input("Enter account name: ").lower()
    check=dup_accprevention(account)
    if check == 0:
      print("Account Already Exist")
      return

    choice = input("Generate password automatically? (y/n): ").lower()
    if choice == "y":
      password = password_generator()
      if password is None:
        print("Password Not Generated\n")
        while password is None:
           password = password_generator()

      else:
        password = input("Enter the password: ")

    with open("password.txt", "a") as file:
      file.write(f"{account} | {password}\n")

    print("Password Added Successfully!\n")


def view_accounts():
    try:
        with open("password.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("No account found.\n")
                return
            print("Saved Accounts:")
            for line in lines:
                account = line.split("|")[0].strip()
                print(f"- {account}")
            print()
    except FileNotFoundError:
        print("No file found.\n")

def search_password():
    searched = input("Enter the account name for password: ").lower()
    found = False
    try:
        with open("password.txt", "r") as file:
            lines = file.readlines()

        if not lines:
            print("No account found.\n")
            return

        for line in lines:
            account, password = line.split("|")
            account = account.strip()
            password = password.strip()
            if searched == account:
                masked = "*" * len(password)
                print(f"Password for {account}: {masked}")
                found = True
                break

        if not found:
            print("No account found")

    except FileNotFoundError:
        print("No file found.\n")

def view_password():
    searched = input("Enter account name: ").lower()
    found = False

    try:
        with open("password.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            account, password = line.split("|")
            account = account.strip()
            password = password.strip()

            if searched == account:
                print(f"Password for {account}: {password}")
                found = True
                break

        if not found:
            print("No account found.")

    except FileNotFoundError:
        print("No file found.\n")

def update_password():
    searched = input("Enter the account name to update: ").lower()
    newpassword = input("Enter the new password: ")
    found = False
    try:
        with open("password.txt", "r") as file:
            lines = file.readlines()

        for i in range(len(lines)):
            account, password = lines[i].split("|")
            account = account.strip()

            if searched == account:
                lines[i] = f"{account} | {newpassword}\n"
                found = True
                break

        if found:
            with open("password.txt", "w") as file:
                file.writelines(lines)
            print("Password updated successfully!\n")
        else:
            print("No such account found.\n")

    except FileNotFoundError:
        print("No file found.\n")

def delete_password():
    searched = input("Enter account name to delete: ").lower()
    deleted = False
    try:
        with open("password.txt", "r") as file:
            lines = file.readlines()

        new_lines = []
        for line in lines:
            account, password = line.split("|")
            if account.strip() != searched:
                new_lines.append(line)
            else:
                deleted = True

        with open("password.txt", "w") as file:
            file.writelines(new_lines)

        if deleted:
            print("Account deleted successfully!\n")
        else:
            print("Account not found.\n")

    except FileNotFoundError:
        print("No file found.\n")

create_master_password()
if not login():
    exit()

while True:
    show_menu()
    choice = input("Enter the choice: ")
    if choice == "1":
        add_password()
    elif choice == "2":
        view_accounts()
    elif choice == "3":
        search_password()
    elif choice == "4":
        view_password()
    elif choice == "5":
        update_password()
    elif choice == "6":
        delete_password()
    elif choice == "7":
        password_generator()
    elif choice == "8":
        print("GOODBYE!")
        break
    else:
        print("Enter a Valid Choice")
