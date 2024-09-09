class Banking:
    def __init__(self):
        self.accounts = {}

    def createaccount(self,accountid,initialamt = 0):
        if accountid in self.accounts:
            return "account already exsiists"
        else:
            self.accounts[accountid] = initialamt
            return f" accounf created successfully with insital amount {initialamt} and amount is {self.accounts[accountid]}"

    def makedeposit(self,accountid,depositamount):
        if accountid in self.accounts and depositamount >0:
            self.accounts[accountid] +=depositamount
            return f"account existed  and amount is successfully deposited {self.accounts[accountid]}"
        else:
            return " account does not exist"
    def withdrawal(self,accountid,withdrawamount):
        if accountid in self.accounts and withdrawamount > 0:
            self.accounts[accountid] -= withdrawamount
            return f"account existed  and amount is successful withdraw done{self.accounts[accountid]}"
        else:
            return " account does not exist"
    def checkBalance(self,accountid):
        if accountid not in self.accounts:
            return "account doesnot exsiists"

        else:
            return self.accounts[accountid]


transaction1 = Banking()
print(transaction1.createaccount(123,100))
print(transaction1.checkBalance(123))

print (transaction1.withdrawal(123,50))
print(transaction1.checkBalance(123))

print (transaction1.makedeposit(123,20000))
print(transaction1.checkBalance(123))