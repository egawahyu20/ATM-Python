class ATMCard:

    def __init__(self, defaultPin, defaultBalance):
        self.pin = defaultPin
        self.balance = defaultBalance

    def checkPin(self):
        return self.pin

    def checkBalance(self):
        return self.balance