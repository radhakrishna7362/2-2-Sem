class BankAccount:
    def __init__(self,accno):
        self.accountno=accno
    def get_Account(self):
        return str(self.accountno)
class MobileBankAccount(BankAccount):
    def __init__(self,accno,pin,balance):
        super().__init__(accno)
        self.pin=pin
        self.accBalance=balance
    def AccountDetails(self):
        return "AccountNo = "+super().get_Account()+"\n"+"Balance = "+str(self.accBalance)
class InternetBankAccount(BankAccount):
    def __init__(self,accno,pin,balance):
        super().__init__(accno)
        self.pin=pin
        self.accBalance=balance
    def AccountDetails(self):
        return "AccountNo = "+super().get_Account()+"\n"+"Balance = "+str(self.accBalance)
if __name__=="__main__":
    acc1=MobileBankAccount(123456789,5643,20000)
    print("Mobile Bank Account")
    print(acc1.AccountDetails())
    print()
    acc2=InternetBankAccount(987654321,3465,10000)
    print("Internet Bank Account")
    print(acc2.AccountDetails())
    
