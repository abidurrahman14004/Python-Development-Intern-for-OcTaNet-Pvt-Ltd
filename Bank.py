import time

print("Please insert Your CARD")
time.sleep(5)

password = 1234
balance = 5000

try:
    pin = int(input("Enter Your ATM pin: "))
except ValueError:
    print("Invalid input. Please enter a numeric pin.")
    exit()

if pin == password:
    while True:
        print(
            """
            1 == Balance
            2 == Withdraw Balance
            3 == Deposit Balance
            4 == Exit
            """
        )

        try:
            option = int(input("Please enter your choice: "))
        except ValueError:
            print("Please enter a valid option.")
            continue

        if option == 1:
            print(f"Your current balance is {balance}")

        elif option == 2:
            try:
                withdraw_amount = int(input("Please enter the withdraw amount: "))
                if withdraw_amount > balance:
                    print("Insufficient balance!")
                else:
                    balance -= withdraw_amount
                    print(f"{withdraw_amount} is debited from your account.")
                    print(f"Your updated balance is {balance}")
            except ValueError:
                print("Invalid input. Please enter a numeric amount.")

        elif option == 3:
            try:
                deposit_amount = int(input("Please enter the deposit amount: "))
                balance += deposit_amount
                print(f"{deposit_amount} is credited to your account.")
                print(f"Your updated balance is {balance}")
            except ValueError:
                print("Invalid input. Please enter a numeric amount.")

        elif option == 4:
            print("Thank you for using our service.")
            break

        else:
            print("Please enter a valid option.")
else:
    print("Wrong pin. Please try again.")
