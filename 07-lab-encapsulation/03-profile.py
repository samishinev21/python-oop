class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username
    
    @property
    def password(self):
        return self.__password

    @username.setter
    def username(self, value):
        if 5 < len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @password.setter
    def password(self, value):
        if len(value) < 8 or not self.has_digit(value) or not self.has_upper(value):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        
        self.__password = value

    def has_digit(self, value):
        for character in value:
            if character.isnumeric():
                return True
            
        return False
    
    def has_upper(self, value):
        for character in value:
            if character.upper():
                return True
            
        return False
    
    def __str__(self):
        return f"You have a profile with username: \"{self.__username}\" and password: {'*' * len(self.__password)}"