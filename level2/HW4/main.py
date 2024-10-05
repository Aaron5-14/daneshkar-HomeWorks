from users import User

def sign_up_menu():
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
        print(new_user.error())
        print("0. Back\n1. Try Again")    
        user_input = input("Input: ")
        if user_input == '1':
            sign_up_menu()
        else:
            return


def log_in_menu():
    username = input("Username: ")
    password = input("Password: ")
    user = User(username, password)
    
    if user.log_in():
        


while True:
    print("0. Quit\n1. Sign Up\n2. Log In")
    user_input = input("Input: ")
    if user_input == '0':
        exit(0)

    elif user_input == '1':
        sign_up_menu()        

    elif user_input == '2':
        log_in_menu()
