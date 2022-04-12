class Account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def __str__(self):
        return f'Account owner {self.owner}\nAccount balance {self.balance}' 
    def deposit(self,deposit_amt):
        self.balance+=deposit_amt
        print("Deposited the amount and the new balanace is {}".format(self.balance)) 
    def withdraw(self,withdraw_amt):
        if withdraw_amt>self.balance:
            print("withdraw amount exceeds current balance")
            return
        self.balance-=withdraw_amt   
        print("withrawal accepted and the new balance is {}".format(self.balance)) 

bank_acct=Account('raj',1000)
print(bank_acct)
bank_acct.deposit(500)
bank_acct.withdraw(50)
