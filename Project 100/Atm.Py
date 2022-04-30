
class ATM: 
    """
        creditals for atm
    """
    def __init__(self,cardNumber,pin):
        self.cardNumber = cardNumber
        self.pin = pin
    
    def check_Balance(self):
        print("Your balance is 1000 dollars.")

    def withdraw(self,amount):
        new_amount = 1000 - amount
        print("You have withdrawn amount "+ str(amount)+". your remaining balance is" + str(new_amount) )

def main():
    card_Number = input("Insert your card number:")
    pin_Number = input("Enter your PIN number:")
    new_user = ATM(card_Number,pin_Number)
    print("Choose your activity:")
    print("1. balance equirry 2. withdraw")
    activity = int(input("Enter Activity Number:"))
    if(activity == 1):
        new_user.check_Balance()
    elif(activity == 2):
        amount = int(input("Enter the amount:"))
        new_user.withdraw(amount)
    else:
        print("Enter a vaild number please.")
if __name__ == "__main__" :
    main()
