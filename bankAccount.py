class BankAccount:
  all_accounts = []
  def __init__(self, int_rate, balance):
    self.int_rate = int_rate
    self.balance = balance
    # BankAccount.all_accounts.append(self)

#increases the account balance by the given amount
  def deposit(self, amount):
    self.balance += amount
    return self

#decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
  def withdraw(self, amount):
      if amount < self.balance:
          self.balance -= amount
      else:
          print("Insufficient funds: Charging a $5 fee")
      self.balance -= 5
      print(f"Your new balance is: ${self.balance}") 
      return self

#print to the console: eg. "Balance: $100"
  def display_account_info(self):
    print(f"Interest Rate is: {self.int_rate*100}%")
    print(f"Your final balance with the interest rate is: ${self.balance}")
    return self

#increases the account balance by the current balance * the interest rate (as long as the balance is positive)
  def yield_interest(self):
    self.balance *= (1+ self.int_rate)
    print(f"${self.balance}")
    return self

user1_account = BankAccount(0.07, 0)
user2_account = BankAccount(0.04, 0)

user1_account.deposit(55).deposit(180).deposit(20).withdraw(50).yield_interest().display_account_info()
print("=================") # i wrote this here so i would have a space between the users so i can read it better when it prints out
user2_account.deposit(700).deposit(50).withdraw(50).withdraw(30).withdraw(150).withdraw(5).yield_interest().display_account_info()


#To the first account, make 3 deposits and 1 withdrawal,
# then yield interest and display the account's info all
# in one line of code (i.e. chaining)