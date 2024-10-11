"""
The users class which maanges user information storage and 
authentication. It acts similar to login signup systems.
"""
import hashlib
import uuid
class User:
    """
    A class to represent a user management system.

    This class allows users to register, log in, and modify their account 
    information (username, password, phone number). It handles validation, 
    stores registered users, and provides error handling.

    Attributes:
    -----------
    registered_users : dict
        A dictionary to hold all registered users' information (e.g., id, username, password, etc.).
    error_message : str
        A string to accumulate error messages during validation or operation.
    _username : str
        The username of the user.
    __password : str
        The user's password (stored as a private attribute).
    _phone_number : str            
        The user's phone number (optional).
    _id : str
        The user's unique identifier (generated upon registration).
        
    Methods:
    --------
    __init__(self, username, password, phone_number=None):
        Initializes a new user object.
        
    error(cls):
        Returns the accumulated error message.
        
    __str__(self):
        Returns the user's information as a formatted string.
        
    username(self):
        Returns the username of the user.
        
    change_username(self, username):
        Validates and updates the username of the user.
        
    password(self):
        Returns the password of the user (hashed).
        
    change_password(self, password):
        Validates and updates the password of the user.
        
    phone_number(self):
        Returns the user's phone number.
        
    change_phone_number(self, phone_number):
        Validates and updates the user's phone number.
        
    register(self):
        Validates and registers the user, adding them to the list of registered users.
        
    login(self):
        Logs the user in by validating their credentials and loading their data.
    """
    
    # Class Attributes
    registered_users = {}
    error_message = ''
    # Constructor
    def __init__(self, username: str, password: str, phone_number: str = None) -> None:
        """
        Initializes the User object with the provided username, password,
        and optional phone number.

        Parameters
        ----------
        username : str 
            The username for the user.
        password : str
            The password for the user.
        phone_number : str, optional
            The phone number of the user (default is None).
        """
        self._username = username
        self.__password = password
        self._phone_number = phone_number  
        self._id = None

    @classmethod
    def error(cls) -> str:
        """
        Returns the error_message class variable.
        """
        return cls.error_message    
      
    def __str__(self) -> str:
        """
        Returns user information in a formatted string.
        """
        return f"Id: {self._id}\nUsername: {self._username}\nPhone Number: {self._phone_number}"
    
    # Username
    @property
    def username(self) -> str:
        """
        Returns username of the user.
        """        
        return self._username
    
    @staticmethod
    def _validate_username(username: str) -> bool:
        """
        Validates username for length and if it is available.

        Parameters
        ----------
        username : str
            username to validate

        Returns
        -------
        bool
            True if valid, otherwise False.
        """
        if len(username) < 5:
            User.error_message += "UserError: Username needs to have at least 5 characters."
            return 0   
                     
        for value in User.registered_users.values():
            if value['Username'] == username:
                User.error_message += "UserError: Username already in use."
                return 0 

        return True        

    def change_username(self, username: str) -> bool:
        """
        Validates and changes the user's username if 
        the username is valid and not already in use.

        Parameters
        ----------
        username : str
            The new username to assign.

        Returns
        -------
        bool
            True if the username was successfully changed, 
            False if validation fails.
        """
        User.error_message = ''
        if self._id == None:
            User.error_message += "UserError: Not Logged in."
            return False
                
        if not self._validate_username(username):
            return False
        
        self._username = username
        User.registered_users[self._id]['Username'] = username
        return True
    
    # Password
    @staticmethod
    def _hash_password(password: str) -> bool:
        """
        Hashes password using sha256 algorithm.

        Parameters
        ----------
        password : str
            The password to hash.

        Returns
        -------
        str
            Hashed password
        """
        return hashlib.sha256(password.encode()).hexdigest()

    @property
    def password(self) -> str:
        """
        Returns user password
        """
        return self.__password
    
    @staticmethod
    def _validate_password(password: str) -> bool:
        """
        Validates password for length.

        Parameters
        ----------
        password : str
            password to validate

        Returns
        -------
        bool
            True if valid, otherwise False.
        """        
        if len(password) < 5:
            User.error_message += "UserError: Password needs to have at least 5 characters."
            return 0        
        
        return True
    
    def change_password(self, password: str) -> bool:
        """
        Validates and changes the user's password after hashing it.

        Parameters
        ----------
        password : str
            The new password to assign.

        Returns
        -------
        bool
            True if the password was successfully changed,
            False if validation fails.
        """
        User.error_message = ''
        if self._id == None:
            User.error_message += "UserError: Not Logged in."
            return False
                
        if not self._validate_password(password):
            return False
        
        self.__password = self._hash_password(password)
        User.registered_users[self._id]['Password'] = self.__password
        return True    
                
    # Phone Number
    @property
    def phone_number(self) -> str:
        """
        Returns user phone number
        """
        return self._phone_number
        
    @staticmethod
    def _validate_phone_number(phone_number: str) -> bool:
        """
        Validates phone number for length and if it is all numeric.

        Parameters
        ----------
        phone number : str
            phone number to validate

        Returns
        -------
        bool
            True if valid, otherwise False.
        """            
        if phone_number == None:
            return True
        
        if 0 < len(phone_number) < 5:
            User.error_message += "UserError: Phone number needs to have at least 5 digits."
            return 0

        if len(phone_number) >= 5:   
            for digit in phone_number:
                if not digit.isnumeric():
                    User.error_message += "UserError: Phone number can only have numeric digits."
                    return 0

        return True        

    def change_phone_number(self, phone_number: str) -> bool:
        """
        Validates and changes the user's phone number.

        Parameters
        ----------
        phone_number : str
            The new phone number to assign.

        Returns
        -------
        bool
            True if the phone number was successfully changed,
            False if validation fails.
        """
        User.error_message = ''
        if self._id == None:
            User.error_message += "UserError: Not Logged in."
            return False
                
        if not self._validate_phone_number(phone_number):
            return False
        
        self._phone_number = phone_number
        User.registered_users[self._id]['Phone Number'] = phone_number
        return True   
               
    # register
    @staticmethod
    def _full_validate(username: str, password: str, phone_number=None) -> bool:
        """
        Validates username, password and phone number.

        Parameters
        ----------
        username : str
        password : str
        phone_number : str

        Returns:
        bool
            True if valid, otherwise False
        """
        flag_username = User._validate_username(username)
        flag_password = User._validate_password(password)
        flag_phone_number = User._validate_phone_number(phone_number)
        if flag_username and flag_password and flag_phone_number:
            return True

        return False    

    def register(self) -> bool:
        """
        Validates and registers the user by adding them to the list 
        of registered users.

        The method validates the username, password, and phone number. 
        If validation passes, the user is assigned a unique ID and added
        to the 'registered_users' dictionary.

        Returns
        -------
        bool
            True if registration was successful, False if validation fails.
        """
        User.error_message = ''
        if not self._full_validate(self.username, self.__password, self._phone_number):
            return False

        self._id = str(uuid.uuid4())
        self.__password = self._hash_password(self.__password)
        User.registered_users[self._id] = {'Username': self._username, 'Password': self.__password, 'Phone Number': self._phone_number} 
        return True

    # login
    def login(self) -> bool:
        """
        Authenticates the user by checking the username and password.

        The method checks if the provided username and hashed password match
        an entry in 'registered_users'. If a match is found, the user’s 
        information is loaded into the current instance.

        Returns
        -------
        bool
            True if login is successful,
            False if the credentials are incorrect or the user does not exist.
        """
        User.error_message = ""
        hashed_password = self._hash_password(self.__password)
        for key, value in User.registered_users.items():
            if value['Username'] == self._username:
                if value['Password'] == hashed_password:
                    self._id = key
                    self.__password = hashed_password
                    self._phone_number = value['Phone Number']
                    return True
                else:
                    User.error_message += "UserError: Incorrect Password."
                    return False

        User.error_message += 'UserError: This username does not exist.'
        return False                


        

