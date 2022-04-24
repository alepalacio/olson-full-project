# Random password generator

class RandomPassword():

    def __init__(self):
        self.password = self.get_random_password()
    
    def get_random_password(self):
        import random
        import string

        alpha = string.ascii_letters
        numbers = string.digits
        characters = string.punctuation
        chars = f"{alpha}{numbers}{characters}"
        pass_length = 15
        password = ""

        for char in range(pass_length):
            password += random.choice(chars)
        return password

    def __str__(self):
        return self.password

