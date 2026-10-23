import random

BankBalance = 10000

usrname = input("Enter your username: ")
password = input("Enter your password: ")

if usrname == "rushi" and password == "6780":
    print("Username and password verified ✅")

    generatedOTP = random.randint(1000, 9999)
    print("Your OTP is", generatedOTP)

    otp = int(input("Enter your OTP: "))

    if otp == generatedOTP:
        print("============= Welcome to Banking App =============")

        while True:
            print("\n1. Check balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                print("Your balance is Rs", BankBalance)

            elif choice == 2:
                amount = int(input("Enter deposit amount: "))

                if amount > 0:
                    BankBalance += amount
                    print("Deposit successful ✅")
                    print("After deposit your balance is Rs", BankBalance)
                else:
                    print("Invalid amount ❌")

            elif choice == 3:
                withdraw = int(input("Enter withdraw amount: "))

                if withdraw > 0:
                    if withdraw <= BankBalance:
                        BankBalance -= withdraw
                        print("Withdraw successful ✅")
                        print("After withdraw your balance is Rs", BankBalance)
                    else:
                        print("Insufficient balance ❌")
                else:
                    print("Invalid amount ❌")

            elif choice == 4:
                print("Thank you for banking with us! 😊")
                break

            else:
                print("Invalid choice ❌")

    else:
        print("Incorrect OTP ❌")

else:
    print("Incorrect username or password ❌")