# # print("Welcome to Chase bank.")
# # print("Have a nice day!")

balance = 10000

def view_balance(balance):
  print('Your current balance is {}'.format(balance)) 

def withdraw(balance):
  amount = input('How much money would you like to withdraw?\n')
  amount = int(amount)
  if amount > balance:
    print('Insufficient funds')
  elif amount == balance:
    print('Thats all yr dang money though!\n')
  else:
    print('Successfully withdrew {} dollars\n'.format(amount))
    print('Your remaining balance is {}\n'.format(balance - amount))
    return balance - amount

def deposit(balance):
  amount = input('How much money would you like to deposit?\n')
  amount = int(amount)
  print('Successfully deposited {} dollars \n'.format(amount))
  print('Your current balance is {} dollars \n'.format(balance + amount))
  return balance + amount


def again(balance):
  done = input('Are you done? y/n \n')
  if 'y' in done:
    print('Thank you!')
  elif 'n' in done:
    banking(balance)


def banking(balance):
  user_input = input('View Balance, Withdraw, or Deposit?\n')
  if user_input.lower() == 'v':
    view_balance(balance)
  elif user_input.lower() == 'w':
    print('Lets withdraw some dang money\n') 
    balance = withdraw(balance)
  elif user_input.lower() == 'd':
    balance = deposit(balance)
  else:
    print('command not found, please press w, v, or d')
  again(balance)

banking(balance)