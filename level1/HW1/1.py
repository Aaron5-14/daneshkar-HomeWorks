username = input("Username: ")
password = input("Password: ")
if username == 'admin' and password == 'admin':
    print('Welcome')
elif username == 'admin':
    print('Wrong Data')
else:
    print(f"Hello {username}")        