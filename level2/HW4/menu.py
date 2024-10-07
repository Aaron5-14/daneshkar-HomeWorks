from users import *
import os
import platform

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def sign_up_menu():
    clear_screen()
    username = input("Username: ")
    password = input("Password: ")
    phone_number = input("Phone number: ")
    if len(phone_number) == 0:
        new_user = User(username, password)
    else:
        new_user = User(username, password, phone_number)

    if new_user.register():
        print("Account created!\n0. Back\n1. Log in")
        user_input = input("Input: ")
        if user_input == '1':
            log_in_menu()
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


def log_in_menu():
    clear_screen()
    username = input("Username: ")
    password = input("Password: ")
    user = User(username, password)
    
    if user.log_in():
        clear_screen()
        print("Successfully Logged In!\n0. Continue")
        usr_input = input("Input: ")
        user_panel(user)
    else:
        print(user.error)
        print("0. Back\n1. Try Again")
        usr_input = input("Input: ")   
        if usr_input == '0':
            return
        else: 
            log_in_menu()
         
        


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
                new_username = input("New Username: ")
                if user.set_username(new_username):
                    print(f"Username successfully changed to {new_username}")
                else:
                    clear_screen()
                    print(user.error)
                    print("0. Back")    
                    usr_input = input("Input: ")
            elif usr_input == '2':
                new_phone_number = input("New Phone Number: ")        
                if user.set_phone_number(new_phone_number):
                    print(f"Phone number successfully changed to {new_phone_number}")
                else:
                    clear_screen()
                    print(user.error)                   
                    print("0. Back")    
                    usr_input = input("Input: ")
        elif user_input == '3':
            #get password and verify using static method