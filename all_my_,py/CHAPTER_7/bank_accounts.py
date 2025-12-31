
#Bank acout 


class Student: 
  def __init__(self, name, year, enrolled, gpa):
    self.name = name
    self.year = year
    self.enrolled = enrolled
    self.gpa = gpa
  
  def display_info(self):
    print('The student ' + self.name + '\'s GPA is ' + str(self.gpa) + '!')
    
  # this is what codex wanted   
class BankAccount:
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_typem = account_type
    self.pin = pin
    self.balance =  balance
    
    
  def deposit(self, amount):
    self.balance += amount
    return self.balance
  
  def withdraw(self,amount):
    self.balance -= amount 
    return self.balance
  
  def display_balance(self):
    print(f"Current balance: ${self.balance:.2f}")



checking_account = BankAccount("Jane", "Doe", 13243546, "checking", 0000, 250.00)


checking_account.deposit(100)

checking_account.withdraw(100)

checking_account.display_balance()

#this is the origanal version 
class BankAccount:
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_typem = account_type
    self.pin = pin
    self.balance =  balance
    
    
  def deposit(self, amount):
    amount = int(input('How much would you like to deposit:'))
    self.balance += amount
    return self.balance
  
  def withdraw(self,amount):
    amount = int(input("how much would you like to withdraw:"))
    self.balance -= amount 
    return self.balance
  
  def display_balance(self):
    print(f"Current balance: ${self.balance:.2f}")



checking_account = BankAccount("Jane", "Doe", 13243546, "checking", 0000, 250.00)


checking_account.deposit(checking_account)

checking_account.withdraw(checking_account)

checking_account.display_balance()