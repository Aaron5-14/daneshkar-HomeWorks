class User:
    registered_users = {}
    def __init__(self, username, password, phone_number = None):
        self.username = username
        self.password = password
        self.phone_number = phone_number
        self.logged_in = 0

    def register(self):
        pass

    @property
    def logged_in(self):
        return self.logged_in    