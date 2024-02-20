class User:
    def __init__(self, name, password, mail):
        self.name = name
        self.password = password
        self.mail = mail

    def info(self):
        return "username: {}, password: {}, mail : {}".format(self.name, self.password, self.mail)
