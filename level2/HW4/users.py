class User:
    registered_users = {}
    def __init__(self, username, password, phone_number = None):
        self._username = username
        self.__password = password
        self._phone_number = phone_number
        self._logged_in = False
        self._error = None        

    def register(self):
        pass

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
            self._error = "UserError: Password needs to have at least 4 characters."
            return 0
        
        self.__password = new_password
        return True
    
    def log_in(clss,a):
        return clss + a

