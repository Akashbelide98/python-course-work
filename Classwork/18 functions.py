
def menu():
    print('[C]heck balance ')
    print('[D]eposit')
    print('[W]ithdraw')
    print('[V]iew Transactions History')
    print('[E]xit\n')
def Welcome():
    print(' Welcome to ATM '.center(40,'*'))

Welcome()
menu()

def Withdraw():
    amount=int(input("Emter the amount to withdraw:"))
    if amount<=data['current_balance']:
        data['current_balance']-=amount
        data['history'].append()