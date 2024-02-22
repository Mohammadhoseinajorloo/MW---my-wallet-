class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def info(self):
        return "username: {}, password: {}".format(self.name, self.password)
