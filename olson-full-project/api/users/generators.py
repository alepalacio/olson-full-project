# Random password generator

def get_random_password():
    import random
    import string

    alpha = string.ascii_letters
    numbers = '0123456789'
    chars = f"{alpha}{numbers}"
    pass_length = 15

    password = ""

    for char in range(pass_length):
        password += random.choice(chars)
    return password

