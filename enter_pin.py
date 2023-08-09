print('''
Bank of Beingsie
    ''')

# Ask user for PIN
pin = int(input("Enter your PIN: "))

# While Loop
while pin != 1234:
    print('''
Incorrect PIN.
    ''')
    pin = int(input("Please enter your PIN again: "))
    
if pin == 1234:
    print('''
PIN accepted!
    ''')