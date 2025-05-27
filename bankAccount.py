class BankAccount:
	def __init__(self, ownerName):
		self.ownerName = ownerName
		self.balance = 0.0
		self.transactions = []
		self.loan_amount = 0.0
		self.is_frozen = False
		self.min_balance = 0.0

	def deposit(self, amount):
		if amount <= 0:
			return "Deposit amount must be positive."
		if self.is_frozen:
			return "Account is frozen. Cannot deposit."
		self.balance += amount
		self.transactions.append(f"Deposited amount: {amount}")
		return f"Dear {self.ownerName} your account has been deposited {self.balance} Birr."

	def withdraw(self, amount):
		if amount <= 0:
			return f"Dear {self.ownerName} Withdrawal amount must be positive."
		if self.is_frozen:
			return "Account is frozen. Cannot withdraw."
		if self.balance - amount < self.min_balance:
			return "Cannot withdraw: balance would fall below minimum balance."
		self.balance -= amount
		self.transactions.append(f"Withdrew: {amount} Birr")
		return f"Current balance: {self.balance}"

	def transfer_funds(self, amount, optional_account):
		if amount <= 0:
			return "Transfer amount must be positive."
		if self.is_frozen or optional_account.is_frozen:
			return "One of the accounts is frozen. Cannot transfer funds."
		if self.balance - amount < self.min_balance:
			return "Cannot transfer: balance would fall below minimum balance."
		self.balance -= amount
		optional_account.balance += amount
		self.transactions.append(f"Transferred: {amount} to {optional_account.ownerName}")
		optional_account.transactions.append(f"Received: {amount} from {self.ownerName}")
		return f"Dear {self.ownerName} your account has {self.balance} Birr."

	def get_balance(self):
		return f"Dear {self.ownerName}, your balance is {self.balance}"
	
	def request_loan(self, amount):
		if amount <= 0:
			return "Loan amount must be positive."
		self.loan_amount += amount
		self.transactions.append(f"Loan requested: {amount}")
		return f"Loan approved. Total loan amount: {self.loan_amount}"
	
	def repay_loan(self, amount):
		if amount <= 0:
			return "Repayment amount must be positive."
		if amount > self.loan_amount:
			return "Cannot repay more than the loan amount."
		self.loan_amount -= amount
		self.transactions.append(f"Loan repaid: {amount}")
		return f"Remaining loan amount: {self.loan_amount}"
	
	def view_account_details(self):
		return {
        	"Owner": self.ownerName,
        	"Balance": self.balance,
        	"Loan Amount": self.loan_amount,
        	"Frozen": self.is_frozen,
        	"Minimum Balance": self.min_balance,
        	"Transactions": self.transactions
    	}

	def change_account_owner(self, new_owner):
		self.ownerName = new_owner
		return f"Account owner changed to: {self.ownerName}"

	def account_statement(self):
		statement = "Account Statement:\n"
		for transaction in self.transactions:
			statement += transaction + "\n"
		return statement

	def interest_calculation(self):
		interest = self.balance * 0.05
		self.balance += interest
		self.transactions.append(f"Interest applied: {interest}")
		return f"New balance after interest: {self.balance}"

	def freeze_account(self):
		self.is_frozen = True
		return "Account has been frozen."

	def unfreeze_account(self):
		self.is_frozen = False
		return "Account has been unfrozen."

	def set_minimum_balance(self, amount):
		if amount < 0:
			return "Minimum balance cannot be negative."
		self.min_balance = amount
		return f"Minimum balance set to: {self.min_balance}"

	def close_account(self):
		self.balance = 0.0
		self.transactions.clear()
		self.loan_amount = 0.0
		return "Account closed. All balances and transactions have been reset."
	
firstAccount = BankAccount("Birhanu Tekulu")
secondAccount = BankAccount("Rahel Welu")

print(firstAccount.deposit(100000))
print(firstAccount.withdraw(30000))
print(firstAccount.transfer_funds(50000, secondAccount))
print(firstAccount.get_balance())
print(firstAccount.get_balance())
print(firstAccount.request_loan(20000))
print(firstAccount.repay_loan(25000))
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