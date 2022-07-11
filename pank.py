"""This module is define the Bank class"""
import pickle
from savingAcount import SavingAccount

class Bank(object):
    def __int__(self, fileName = None):
        self.accounts = {}
        self.fileName = fileName
        if fileName != None:
            fileObj = open(fileName, "rb")
            while True:
                try:
                    account = pickle.load(fileObj)
                    self.add(account)
                except EOFError:
                    fileObj.close()
                    break
        
    def __str__(self):
        return "\n".join(map(str, self.accounts.values()))
    
    def makeKey(self, name, pin):
        return name + "/" + pin
    
    def add(self, account):
        key = self.makeKey(account.getName(), account.getPin())
        self.accounts[key] = account
        
        
    def remove(self, name , pin):
        key = self.makeKey(name, pin)
        return self.accounts.pop(key,None)
    
    def get(self, name ,pin):
        key = self.makeKey(name, pin)
        return self.accounts.get(key, None)
    
    def computeInterset(self):
        """Compute interset for all account and return the total."""
        total = 0.0
        for account in self.accounts.values():
            total += account.computeInterset()
            return total
