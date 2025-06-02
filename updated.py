from datetime import datetime

class Transaction:
    def __init__(self, narration, amount, transaction_type):
        self.date_time = datetime.now()
        self.narration = narration
        self.amount = amount
        self.transaction_type = transaction_type  
    
    def __str__(self):
        return f"{self.date_time.strftime('%Y-%m-%d %H:%M:%S')} | {self.transaction_type.upper()} | {self.narration} | Amount: {self.amount}"

class Account:
    def __init__(self, owner_name, account_number):
        self.owner_name = owner_name
        self.__account_number = account_number
        self.__transactions = []
        self.__loan_amount = 0.0
        self.__is_frozen = False
        self.__min_balance = 0.0
    @property
    def account_number(self):
        return self.__account_number

    @property
    def is_frozen(self):
        return self.__is_frozen

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be positive."
        if self.__is_frozen:
            return "Account is frozen. Cannot deposit."
        self.__transactions.append(Transaction("Deposit", amount, "deposit"))
        return f"Dear {self.owner_name} your account has been deposited {amount} Birr."

    def withdraw(self, amount):
        if amount <= 0:
            return f"Dear {self.owner_name}, withdrawal amount must be positive."
        if self.__is_frozen:
            return "Account is frozen. Cannot withdraw."
        if self.get_balance() - amount < self.__min_balance:
            return "Cannot withdraw: balance would fall below minimum balance."
        self.__transactions.append(Transaction("Withdrawal", -amount, "withdrawal"))
        return f"Current balance: {self.get_balance()}"

    def transfer_funds(self, amount, optional_account):
        if amount <= 0:
            return "Transfer amount must be positive."
        if self.__is_frozen or optional_account.is_frozen:
            return "One of the accounts is frozen. Cannot transfer funds."
        if self.get_balance() - amount < self.__min_balance:
            return "Cannot transfer: balance would fall below minimum balance."
        self.__transactions.append(Transaction(f"Transferred to {optional_account.owner_name}", -amount, "transfer"))
        optional_account._Account__transactions.append(Transaction(f"Received from {self.owner_name}", amount, "transfer"))
        return f"Dear {self.owner_name} your account has {self.get_balance()} Birr."

    def get_balance(self):
        return sum(tx.amount for tx in self.__transactions)
    
    def request_loan(self, amount):
        if amount <= 0:
            return "Loan amount must be positive."
        self.__loan_amount += amount
        self.__transactions.append(Transaction("Loan requested", amount, "loan"))
        return f"Loan approved. Total loan amount: {self.__loan_amount}"
    
    def repay_loan(self, amount):
        if amount <= 0:
            return "Repayment amount must be positive."
        if amount > self.__loan_amount:
            return "Cannot repay more than the loan amount."
        self.__loan_amount -= amount
        self.__transactions.append(Transaction("Loan repaid", -amount, "loan repayment"))
        return f"Remaining loan amount: {self.__loan_amount}"
    
    def view_account_details(self):
        return {
            "Owner": self.owner_name,
            "Account Number": self.__account_number,
            "Balance": self.get_balance(),
            "Loan Amount": self.__loan_amount,
            "Frozen": self.__is_frozen,
            "Minimum Balance": self.__min_balance,
            "Transactions": [str(tx) for tx in self.__transactions]
        }
#The above View_account_details method shows the whole details of the account where as the next account_statement method shows only the transactions.
    def account_statement(self):
        statement = "Account Statement:\n"
        for tx in self.__transactions:
            statement += str(tx) + "\n"
        return statement

    def interest_calculation(self):
        interest = self.get_balance() * 0.05
        self.__transactions.append(Transaction("Interest applied", interest, "interest"))
        return f"New balance after interest: {self.get_balance()}"

    def freeze_account(self):
        self.__is_frozen = True
        return "Account has been frozen."

    def unfreeze_account(self):
        self.__is_frozen = False
        return "Account has been unfrozen."

    def set_minimum_balance(self, amount):
        if amount < 0:
            return "Minimum balance cannot be negative."
        self.__min_balance = amount
        return f"Minimum balance set to: {self.__min_balance}"

    def close_account(self):
        self.__transactions.clear()
        self.__loan_amount = 0.0
        return "Account closed. All balances and transactions have been reset."
    

firstAccount = Account("Birhanu Tekulu", "12345678")
secondAccount = Account("Rahel Welu", "87654321")
print(firstAccount.deposit(100000))
print(firstAccount.withdraw(30000))
print(firstAccount.transfer_funds(50000, secondAccount))
print(firstAccount.get_balance())
print(firstAccount.request_loan(20000))
print(firstAccount.repay_loan(15000))
print(firstAccount.view_account_details())
print(firstAccount.account_statement())
print(firstAccount.interest_calculation())
print(firstAccount.freeze_account())
print(firstAccount.deposit(20000))  
print(firstAccount.unfreeze_account())
print(firstAccount.deposit(4000))
print(firstAccount.set_minimum_balance(200))
print(firstAccount.withdraw(3000)) 
print(firstAccount.close_account())