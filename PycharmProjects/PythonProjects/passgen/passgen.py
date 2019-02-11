import random, string


class Generator:

    def __init__(self):
        pass

    def generate(self, length):
        self.chars = (string.digits + string.ascii_letters + string.punctuation + string.hexdigits)
        self.password = ''.join(random.choice(self.chars) for i in range(length))
        return self.password

    def savefile(self, name, password):
        with open('Passwords.txt', 'a') as File:
            File.write(name + ': ' + str(password) + '\n')

    def deletefile(self, password):
        pass

passwd = Generator()
passwd.generate(10)
savePass = Generator()
savePass.savefile('Costa', passwd.password)