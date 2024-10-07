class User:
    registered_users = {}
    def __init__(self, username, password, phone_number = None):
        self._username = username
        self.__password = password
        self._phone_number = phone_number
        self._logged_in = False
        self._error = None        

    @property
    def logged_in(self):
        return self.logged_in  

    @logged_in.setter
    def logged_in(self, status):
        self.logged_in = status

    @property
    def error(self):
        return self._error      
      
    def __str__(self) -> str:
        return f"Id: {self.id}\nUsername: {self._username}\nPhone Number: {self._phone_number}"

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        if new_password == self.__password:
            self._error = "UserError: Password Already in Use."
            return 0

        if len(new_password) < 5:
            self._error = "UserError: Password needs to have at least 5 characters."
            return 0
        
        self.__password = new_password
        return True

    def password_validator(func):
        def w(self, new_password):
            if new_password == self.__password:
                self._error = "UserError: Password Already in Use."
                return 0

            if len(new_password) < 5:
                self._error = "UserError: Password needs to have at least 5 characters."
                return 0            

            return func(self, new_password)

        return w

    @password_validator
    def set_password(self, new_password):
        self.__password = new_password
        return True    

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        if new_username == self._username:
            self._error = "UserError: Username already in use."
            return 0
        
        if len(new_username) < 5:
            self._error = "UserError: Username needs to have at least 5 characters."
            return 0
        
        self._username = new_username
        return True

    def username_validater(func):
        def w(self, new_username):
            if new_username == self._username:
                self._error = "UserError: Username already in use."
                return 0
        
            if len(new_username) < 5:
                self._error = "UserError: Username needs to have at least 5 characters."
                return 0                
            
            return func(self, new_username)

        return w 


    @username_validater
    def set_username(self, new_username):
        self._username = new_username
        return True
    
    @property
    def phone_number(self):
        return self._phone_number

    def phone_number_validater(func):
        def w(self, phone_number):
            if len(phone_number) < 5:
                self._error = "UserError: Phone number needs to have at least 5 digits."
                return 0
            
            for digit in phone_number:
                if not digit.isnumeric():
                    self._error = "UserError: Invalid Input."
                    return 0
                
            return func(self, phone_number)    

    @phone_number_validater
    def set_phone_number(self, phone_number):
        self._phone_number = phone_number
        return True        
                

    def register(self):
        