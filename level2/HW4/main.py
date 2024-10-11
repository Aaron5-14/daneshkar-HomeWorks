"""
Name: Ali Shirazi Zamani
Level: 2
Homework: 4
ToDo: Create a user authentication and storage system.
"""
from menu import *
while True:
    clear_screen()
    print("0. Quit\n1. Sign Up\n2. Log In")
    user_input = input("Input: ")
    if user_input == '0':
        exit(0)

    elif user_input == '1':
        sign_up_menu()        

    elif user_input == '2':
        login_menu()
