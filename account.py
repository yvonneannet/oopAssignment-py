class Account:
    def __init__(self, number, pin, owner_name, balance=0, overdraft_limit=0, interest_rate=0.0, minimum_balance=0):
        self.number = number
        self.__pin = pin
        self.owner_name = owner_name
        self.balance = balance
        self.overdraft_limit = overdraft_limit
        self.interest_rate = interest_rate
        self.minimum_balance = minimum_balance
        self.transaction_history = []
        self.frozen = False
        self.__account_status = "Open"
    def account_status(self):
        return self.__account_status
    def show_balance(self, pin):
        if pin == self.__pin:
            return self.balance
        else:
            return "Wrong Pin"
    def view_account_details(self, pin):
        if pin == self.__pin:
            return f"Account Number: {self.number}\nOwner Name: {self.owner_name}\nBalance: {self.balance}\nStatus: {self.account_status()}"
        else:
            return "Wrong Pin"
    def change_account_owner(self, pin, new_owner_name):
        if pin == self.__pin:
            self.owner_name = new_owner_name
            return "Owner information updated successfully"
        else:
            return "Wrong Pin"
    def set_overdraft_limit(self, pin, new_limit):
        if pin == self.__pin:
            self.overdraft_limit = new_limit
            return "Overdraft limit updated successfully"
        else:
            return "Wrong Pin"
    def calculate_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        return f"Interest of {interest_amount} applied. New balance: {self.balance}"
    def freeze_account(self, pin):
        if pin == self.__pin:
            self.frozen = True
            return "Account frozen successfully"
        else:
            return "Wrong Pin"
    def unfreeze_account(self, pin):
        if pin == self.__pin:
            self.frozen = False
            return "Account unfrozen successfully"
        else:
            return "Wrong Pin"
    def transaction_history(self):
        return self.transaction_history
    def set_minimum_balance(self, pin, new_minimum_balance):
        if pin == self.__pin:
            self.minimum_balance = new_minimum_balance
            return "Minimum balance requirement updated successfully"
        else:
            return "Wrong Pin"
    def transfer_funds(self, pin, target_account, amount):
        if pin == self.__pin:
            if not self.frozen:
                if self.balance + self.overdraft_limit - amount >= self.minimum_balance:
                    self.balance -= amount
                    target_account.balance += amount
                    self.transaction_history.append(f"Transferred {amount} to account {target_account.number}")
                    return "Transfer successful"
                else:
                    return "Insufficient funds"
            else:
                return "Account frozen"
        else:
            return "Wrong Pin"
    def close_account(self, pin):
        if pin == self.__pin:
            self.balance = 0
            self.frozen = True
            self.owner_name = "Closed Account"
            self.transaction_history.append("Account closed")
            self.__account_status = "Closed"
            return "Account closed successfully"
        else:
            return "Wrong Pin"





acc1 = Account(number=1999, pin=5000, owner_name="Zach")
print(acc1.view_account_details(5000))
acc1.close_account(5000)
print(acc1.view_account_details(5000))
print(acc1.set_minimum_balance(5000, 5000))
# print(acc1.transaction_history())
print(acc1.freeze_account(5000))
print(acc1.unfreeze_account(5000))
print(acc1.view_account_details(5000))
print(acc1.transfer_funds(5000, acc1, 3000))
print(acc1.view_account_details(5000))
# print(acc1.transaction_history())
acc1.change_account_owner(1999, "Fiona" )