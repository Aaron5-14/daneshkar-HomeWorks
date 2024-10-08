import hashlib
import uuid
class User:
    registered_users = {}
    error = ''
    def __init__(self, username, password, phone_number = None):
        self._username = username
        self.__password = password
        self._phone_number = phone_number
        #self._error = ''       
        self._id = None

    # Username
    @property
    def username(self):
        return self._username
    
    def _validate_username(self, username):
        if len(username) < 5:
            self._error += "UserError: Username needs to have at least 5 characters."
            return 0   
                     
        for value in User.registered_users.values():
            if value['Username'] == username:
                self._error += "UserError: Username already in use."
                return 0 

        return True        

    @username.setter
    def username(self, new_username):
        self._username = new_username
    
    # Password
    @staticmethod
    def _hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, new_password):
        self.__password = new_password

    def _validate_password(self, password):
        if len(password) < 5:
            self._error += "UserError: Password needs to have at least 5 characters."
            return 0        
        
        return True
                
    # Phone Number
    @property
    def phone_number(self):
        return self._phone_number

    def _validate_phone_number(self, phone_number):
        if phone_number == None:
            return True
        
        if 0 < len(phone_number) < 5:
            self._error += "UserError: Phone number needs to have at least 5 digits."
            return 0

        if len(phone_number) >= 5:   
            for digit in phone_number:
                if not digit.isnumeric():
                    self._error += "UserError: Phone number can only have numeric digits."
                    return 0

        return True        

    @phone_number.setter
    def phone_number(self, phone_number):
        self._phone_number = phone_number   

    ###########

    
    @classmethod
    def error(cls):
        return cls.error    #################
      
    def __str__(self) -> str:
        return f"Id: {self._id}\nUsername: {self._username}\nPhone Number: {self._phone_number}"
               
    # register

    def _full_validate(self, username, password, phone_number=None):
        flag_username = self._validate_username(username)
        flag_password = self._validate_password(password)
        flag_phone_number = self._validate_phone_number(phone_number)
        if flag_username and flag_password and flag_phone_number:
            return True

        return False    

    def register(self):
        self._error = ''
        if not self._full_validate(self.username, self.__password, self._phone_number):
            return False

        self._id = str(uuid.uuid4())
        self.__password = self._hash_password(self.__password)
        User.registered_users[self._id] = {'Username': self._username, 'Password': self.__password, 'Phone Number': self._phone_number} 
        return True

    # login
    def login(self):
        self._error = ""
        hashed_password = self._hash_password(self.__password)
        for key, value in User.registered_users.items():
            if value['Username'] == self._username:
                if value['Password'] == hashed_password:
                    self._id = key
                    self.__password = hashed_password
                    self._phone_number = value['Phone Number']
                    return True
                else:
                    self._error += "UserError: Incorrect Password."
                    return False

        self._error += 'UserError: This username does not exist.'
        return False                

    def change_username(self, username):
        self._error = ''
        if self._id == None:
            self._error += "UserError: Not Logged in."
            return False
                
        if not self._validate_username(username):
            return False
        
        self._username = username
        User.registered_users[self._id]['Username'] = username
        return True
    
    def change_password(self, password):
        self._error = ''
        if self._id == None:
            self._error += "UserError: Not Logged in."
            return False
                
        if not self._validate_password(password):
            return False
        
        self.__password = self._hash_password(password)
        User.registered_users[self._id]['Password'] = self.__password
        return True

    def change_phone_number(self, phone_number):
        self._error = ''
        if self._id == None:
            self._error += "UserError: Not Logged in."
            return False
                
        if not self._validate_phone_number(phone_number):
            return False
        
        self._phone_number = phone_number
        User.registered_users[self._id]['Phone Number'] = phone_number
        return True 
        

