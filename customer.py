from atm_card import ATMCard

class Customer(ATMCard):
    def __init__(self, id, custPin = 1234, custBalance = 10000):
        self.id = id
        super().__init__(custPin, custBalance)

    def checkId(self):
        return self.id

    def withdrawMoney(self, totalWithdraw):
        self.balance -= totalWithdraw

    def depositMoney(self, totalDeposit):
        self.balance += totalDeposit
    
    def changePin(self, newPin):
        self.pin = newPin