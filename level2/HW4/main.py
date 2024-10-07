from users import User
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
    clear_screen()
    print("1. Account Information\n2. Edit Profile\n3. Change Password\n4. Log Out")
    user_input = input("Input: ")
    if user_input == '1':
        clear_screen()
        print(user)
        print('0. Back') 
        usr_input = input("Input: ")
        
    elif user_input == '2':
        user_edit_info_menu()
    elif user_input == '3':
        #get password and verify using static method




while True:
    clear_screen()
    print("0. Quit\n1. Sign Up\n2. Log In")
    user_input = input("Input: ")
    if user_input == '0':
        exit(0)

    elif user_input == '1':
        sign_up_menu()        

    elif user_input == '2':
        log_in_menu()
