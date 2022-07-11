"""Represents an ATM window.
The window tracks the bank and the current account .
The current account is None at the startup and logout"""
from turtle import width
from pank import Bank
from savingAcount import SavingAccount
from breezypythongui import EasyFrame

class ATM(EasyFrame):
    """Represent an ATM window.
    """
    def __init__(self, bank):
        """Initialize the window and establish the data model."""
        EasyFrame.__init__(self,title = "ATM", width=350, height=200)
        self.bank = bank
        self.account = None
        self.addLabel(text= "Name", row=0 , column=0)
        self.namefield = self.addTextField(text = "Name", row=0 , column=1)
        self.balanceButton = self.addButton(text="Balance", row=0, column=2)
        
        self.addLabel(text= "PIN", row=1 , column=0)
        self.pinfield = self.addIntegerField(value=0, row=1 , column=1, width=10)
        self.depositButton = self.addButton(text="Deposit", row=1, column=2)
        
        self.addLabel(text= "Amount", row=2 , column=0)
        self.amountFiel = self.addFloatField(value=0.0, row=2 , column=1)
        self.withdrowButton = self.addButton(text="Withdraw", row=2, column=2)
        
        self.addLabel(text= "Status", row=3 , column=0)
        self.statusField = self.addTextField(text = "Welcome to our Bank!", row=3 , column=1)
        self.logoutButton = self.addButton(text="logout", row=3, column=2)
        self.loginButton = self.addButton(text="login", row=3, column=2, state="")

        
    def login(self):
        """Attempts to login the customer."""
        name = self.nameField.getText()
        pin = self.pinField.getText()
        self.account = self.bank.get(name, pin)
        if self.account:
            self.statusField.setText("Hello, "+ name + "!")
            self.balanceButton["state"] = "normal"
            self.depositButton["state"] = "normal"
            self.withdrowButton["state"] = "normal"
            self.logoutButton["text"] = "logout"
            self.loginButton["command"] = self.logout
            
        else:
            self.statusField.setText("Name and PIN not found")
            
    def logout(self):
        """logs the customer out, clear the fields, 
        display the button, and enables login.
        """
        self.account = None
        self.nameField.setText("")
        self.pinField.setText("")
        self.amountField.setNumber(0.0)
        self.statusField.setText("Wellcome to Our Bank!")
        self.balanceButton["state"] = "display"
        self.depositButton["state"] = "display"
        self.withdrowButton["state"] = "display"
        self.logoutButton["text"] = "login"
        self.loginButton["command"] = self.login
        
        
        
    def getBalance(self):
        """Display the current balance in the status field."""
        balance = self.account.getBalance()
        self.statusField.setText("Balance: $" + str(balance))
        
        
    def withdraw(self):
        """ Attempts a withdrawal. if not successful, 
        display error message in the status field"""
        
        amount = self.amountField.getNumber()
        message = self.account.withdraw(amount)
        if message:
            self.statusField.setText(message)
            
        else:
            self.statusField.setText("Withdrawl successful!")
    

    
        
    
