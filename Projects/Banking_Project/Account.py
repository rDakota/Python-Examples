import random

class Account: 
    def __init__(self, id , balance = 0, annualInterestRate = 0.06):
        self.id = id
        self.balance = balance
        self.annualInterestRate = annualInterestRate

    def getId(self):
        return self.id

    def get_balance(self):
        return self.balance