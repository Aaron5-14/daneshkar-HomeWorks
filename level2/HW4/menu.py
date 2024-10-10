from users import *
import os
import platform
import getpass


def clear_screen() -> None:
    """
    Clears Screen
    """
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def sign_up_menu():
    clear_screen()
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    phone_number = input("Phone number: ")

    if len(phone_number) == 0:
        new_user = User(username, password)
    else:
        new_user = User(username, password, phone_number)

    if new_user.register():
        print("Account created!\n0. Back\n1. Log in")
        user_input = input("Input: ")
        if user_input == '1':
            login_menu()
        else:
            return    
    else:
        print(new_user.error)
        print("0. Back\n1. Try Again")    
        user_input = input("Input: ")
        if user_input == '1':
            sign_up_menu()
        else:
            return

def login_menu():
    clear_screen()
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    user = User(username, password)
    
    if user.login():
        clear_screen()
        print("Successfully Logged In!\n0. Continue")
        usr_input = input("Input: ")
        user_panel(user)
    else:
        print(user.error)
        print("0. Back\n1. Try Again")
        usr_input = input("Input: ")   
        if usr_input == '1':
            login_menu()
        else: 
            return
         
        


def user_panel(user: User):
    while True:
        clear_screen()
        print("1. Account Information\n2. Edit Profile\n3. Change Password\n4. Log Out")
        user_input = input("Input: ")

        if user_input == '1':
            clear_screen()
            print(user)
            print('0. Back') 
            usr_input = input("Input: ")
            continue
        elif user_input == '2':
            clear_screen()
            print("1. Edit Username\n2. Edit phone number")
            usr_input = input("Input: ")
            if usr_input == '1':
                clear_screen()
                username = input("New Username: ")
                if user.change_username(username):
                    print(f"Username successfully changed to {user.username}")
                else:
                    clear_screen()
                    print(user.error)
                    print("0. Back")    
                    usr_input = input("Input: ")
            elif usr_input == '2':
                phone_number = input("New Phone Number: ")        
                if user.change_phone_number(phone_number):
                    print(f"Phone number successfully changed to {user.phone_number}")
                else:
                    clear_screen()
                    print(user.error)                   
                    print("0. Back")    
                    usr_input = input("Input: ")
        elif user_input == '3':
            password = User._hash_password(getpass.getpass("Current Password: "))
            new_password = getpass.getpass("New Password: ")
            repeat_password = getpass.getpass("Repeat Password: ")
            
            if user.password == password and new_password == repeat_password:
                if user.change_password(new_password):
                    clear_screen() #####
                    print(f"Password Successfully updated!")
                    print("0. Back")    
                    usr_input = input("Input: ")
                else:
                    clear_screen()
                    print(user.error)
                    print("0. Back")    
                    usr_input = input("Input: ")   
            elif not user.password == password:
                clear_screen()
                print(password, user.password)
                print("Error: Wrong Password.")
                print("0. Back")    
                usr_input = input("Input: ")                    
            else:
                print("Error: Passwords do not match!")
                print("0. Back")    
                usr_input = input("Input: ")    
        elif user_input == '4':
            clear_screen()
            print("Logged Out!\n1. Continue")
            usr_input = input("Input: ")
            return                
        