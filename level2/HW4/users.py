import hashlib
import uuid
class User:
    registered_users = {}
    def __init__(self, username, password, phone_number = None):
        self._username = username
        self.__password = password
        self._phone_number = phone_number
        self._error = None        
        self._id = None

    # Username

    @property
    def username(self):
        return self._username
    
    def _validate_username(self, username):
        if len(username) < 5:
            self._error = "UserError: Username needs to have at least 5 characters."
            return 0   
                     
        for value in User.registered_users.values():
            if value['Username'] == username:
                self._error = "UserError: Username already in use."
                return 0 

        return True        

    @username.setter
    def username(self, new_username):
        self._username = new_username
    
    # Password

    @property
    def password(self):
        return self.__password

    def _validate_password(self, password):
        if len(password) < 5:
            self._error = "UserError: Password needs to have at least 5 characters."
            return 0        
        
        return True

    @password.setter
    def set_password(self, new_password):
        self.__password = new_password
                       
    def is_password(self, password):
        pass

    # Phone Number

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

    ###########





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

   


    

                
    # register

    def register_validator(func):
        def w(self):
            pass

    def register(self):
        self._id = str(uuid.uuid4())
        if not self._validate_username(self._username):
            User.registered_users[self._id] = {'Username': self._username, 'Password': self.__password, 'Phone Number': self._phone_number} 
            return True


    #def validator:
        #def w(self, *args)


    # login

    def login():
        pass        

    # update

    def update(self):
        pass

    def load(self):
        pass