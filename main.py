from turtle import back
from atm import ATM
from pank import Bank
from savingAcount import SavingAccount

def main(fileName = None):
    if not fileName:
        bank = Bank()
    else:
        bank = Bank(fileName)
    
    atm = ATM(bank)
    atm.mainloop()
    
    
if __name__ == "__main__":
    main()

