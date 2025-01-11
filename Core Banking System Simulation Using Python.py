balance = 1000  # Initial Balance
print("Welcome to XYZ ATM")

while True:  # ATM Interface Loop
    print("\nMain Menu")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    try:
        choice = int(input("Choose an Option from 1 to 4: "))
        
        if choice == 1:
            print("Your Current Balance is: ", balance)
        elif choice == 2:
            deposit = float(input("Enter the Amount to Deposit: "))
            if deposit > 0:
                balance += deposit
                print("Your Balance after Deposit is: ", balance)
            else:
                print("Invalid amount. Please enter a positive amount.")
        elif choice == 3:
            withdraw = float(input("Enter the Amount to Withdraw: "))
            if 0 < withdraw <= balance:
                balance -= withdraw
                print("Your Balance after Withdrawal is: ", balance)
            elif withdraw > balance:
                print("Insufficient funds.")
            else:
                print("Invalid amount. Please enter a positive amount.")
        elif choice == 4:
            print("Thank you for Using the ATM. GOODBYE!")
            break
        else:
            print("Please choose a valid option between 1 and 4.")
    except ValueError:
        print("Invalid Input. Please enter a number between 1 and 4.")
