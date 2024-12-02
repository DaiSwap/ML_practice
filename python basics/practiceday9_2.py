# create account class with 2 attributes - balance and acc num
#create methods for debit,credit&printing the balance

class Accounts:
    def __init__(self,balance,acc_no):
        self.balance = balance
        self.acc_no = acc_no
    def debit(self, amount):
        self.balance -= amount
        print(amount,"was debited")   
        print("total amount",self.get_balance())    
        
    def credit(self, amount):
        self.balance += amount
        print(amount,"was credited")
        print("total amount",self.get_balance())
        
    def get_balance(self):
        return self.balance 

acc1 = Accounts(10000,7890)
acc1.debit(2000)
acc1.credit(10000)
#print(acc1.balance)
#print(acc1.acc_no)
