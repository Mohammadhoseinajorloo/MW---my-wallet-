import random

class Bank_Account:

    total = 0

    def __init__(self, name, ID=None):
        self.name = name
        if ID == None:
            ID = "%04d"%random.randrange(1000)
        self.ID = ID

    def __repr__(self):
        return "name : {}, ID : {}".format(self.name, self.ID)


class CreditCard(Bank_Account):
    def __init__(self, name, name_bank, serial, balance, ID=None):
        super().__init__(name, ID)
        self.name_bank = name_bank
        self.serial = serial
        self.balance = balance


    def __repr__(self):
        return "name_bank : {}, serial : {}, balance : {}".format(self.name_bank, self.serial,                                                                       self.balance)

