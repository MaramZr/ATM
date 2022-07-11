'''this module defines for saving account '''

class SavingAccount(object):
    '''This class is for represent the saving account with the name, PIN and balance'''
    
    RATE = 0.02 #Single rate for account
    
    def __init__(self, name, pin, balance):
        self.name = name
        self.pin = pin
        self.balance = balance
        
    def __str__(self):
        result = "Name: {}\n PIN: {}\n Balance: {}".format(self.name, self.pin, self.balance)
        return result
    
    def getBalance(self):
        return self.balance
    
    def getPin(self):
        return self.pin
    
    
    def getName(self):
        return self.name
    
    def deposit(self, amount):
        '''Deposit the amount and return none'''
        self.balance += amount
        return None
        
        
    def withdrow(self, amount):
        '''Withdrow the given amount '''
        if amount < 0 :
            return "The amount must be more than 0"
        elif amount < self.balance:
            return "Insufficint funds"
        else:
            self.balance -= amount
            
        return None
        
    def computeInterset(self):
        """compute the deposit and return the interset"""
        interset = self.balance * SavingAccount.RATE
        self.deposit(interset)
        return interset
        
    