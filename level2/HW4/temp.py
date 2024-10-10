import hashlib
import uuid

class User:
    registered_users = {}

    def __init__(self, username, password, phone_number=None):
        self._username = username
        self.__password = password
        self._phone_number = phone_number
        self._error = ''  # Initialize as empty string
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

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    # Phone Number
    @property
    def phone_number(self):
        return self._phone_number

    def _validate_phone_number(self, phone_number):
        if phone_number is None:
            return True
        if len(phone_number) < 5:
            self._error += "UserError: Phone number needs to have at least 5 digits."
            return 0
        if not phone_number.isdigit():
            self._error += "UserError: Phone number can only have numeric digits."
            return 0
        return True

    @phone_number.setter
    def phone_number(self, phone_number):
        self._phone_number = phone_number

    ###########
    @property
    def error(self):
        return self._error

    def __str__(self) -> str:
        return f"Id: {self._id}\nUsername: {self._username}\nPhone Number: {self._phone_number}"

    # Register
    def _full_validate(self, username, password, phone_number=None):
        flag_username = self._validate_username(username)
        flag_password = self._validate_password(password)
        flag_phone_number = self._validate_phone_number(phone_number)
        return flag_username and flag_password and flag_phone_number

    def register(self):
        self._error = ''
        if not self._full_validate(self.username, self.__password, self._phone_number):
            return False
        self._id = str(uuid.uuid4())
        hashed_password = self._hash_password(self.__password)
        User.registered_users[self._id] = {'Username': self._username, 'Password': hashed_password, 'Phone Number': self._phone_number}
        return True

    # Login
    def login(self):
        self._error = ""
        hashed_password = self._hash_password(self.__password)
        for key, value in User.registered_users.items():
            if value['Username'] == self._username:
                if value['Password'] == hashed_password:
                    self._id = key
                    self._phone_number = value['Phone Number']
                    return True
                else:
                    self._error += "UserError: Incorrect Password."
                    return False
        self._error += 'UserError: This username does not exist.'
        return False

    # Update
    def update(self):
        if self._id is None:
            self._error += "UserError: Not Logged in."
            return False
        if not self._full_validate(self.username, self.__password, self._phone_number):
            return False
        if self._id in User.registered_users:
            User.registered_users[self._id]['Username'] = self._username
            User.registered_users[self._id]['Password'] = self._hash_password(self.__password)
            User.registered_users[self._id]['Phone Number'] = self._phone_number
            return True
        self._error += "UserError: ID not found."
        return False

    @classmethod
    def load(cls, id):
        if id in cls.registered_users:
            user_data = cls.registered_users[id]
            user = cls(user_data['Username'], user_data['Password'], user_data['Phone Number'])
            user._id = id
            return user
        return None
