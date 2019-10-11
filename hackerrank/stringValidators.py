import os


def hasAlphanumeric(text):
    return any(char.isalnum() for char in text)

def hasAlphabetical(text):
    return any(char.isalpha() for char in text)

def hasDigit(text):
    return any(char.isdigit() for char in text)

def hasLowercase(text):
    return any(char.islower() for char in text)

def hasUppercase(text):
    return any(char.isupper() for char in text)


if __name__ == '__main__':
    pwd = os.getcwd()
    filename = open(pwd + "/string-validators-testcases/input/input00.txt", 'r')

    text = filename.readline().split()[0]
    print(hasAlphanumeric(text))
    print(hasAlphabetical(text))
    print(hasDigit(text))
    print(hasLowercase(text))
    print(hasUppercase(text))