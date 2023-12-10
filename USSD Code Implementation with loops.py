#Assignment
# Create a more advanced short code that's more user friendly. The whole system should be in an infinite loop so user can do it over and over and only end when they choose to quit.

#     When the user enters *123# it should display the menu:
#         Check balance
#         Send money
#         Buy airtime
#     Check balance: i. When user chooses to check balance, they should see their balance. Initial balance is set to 1000. ii. Balance should reduce as and when they send out money or buy airtime.
#     Send money: i. When user chooses to send money, they should be asked to enter amount. Amount can't exceed their current balance. Amount should be a number. Use try-catch (read on it). ii. Each time a user sends money, it should be deducted from their balance.
#     Buy airtime. i. Airtime isn't as you see it. Airtime costs half the actual price. If someone chooses to buy 10gh airtime, they should pay only 5gh. ii. Deduct airtime bought from balance.
#     Make sure your system is user friendly. Put yourself in the shoes of a user and do a great job. I've intentionally left out some details so you can be creative.

# Have fun!!!

# Initialize the user balance to 1000 ghc
user_balance = 1000

while True:
    # Ask the user to enter a code to display the menu or quit the program
    code = input("Enter code *123# to display menu or q to quit program: ")

    # Check if the user wants to display the menu
    if code.strip() == "*123#":
        while True:
            # Ask the user to choose an option from the menu
            choice = input("Enter 1 to check your balance, 2 to send money, 3 to buy airtime, e to exit menu: ")

            # Option 1: Check balance
            if choice.strip() == "1":
                print(f"Your account balance is {user_balance}ghc")

            # Option 2: Send money
            if choice.strip() == "2":
                try:
                    print("You have chosen to send money")
                    amount = float(input("Enter amount to send: "))
                    # Check if the entered amount is negative
                    if amount < 0:
                        print("Amount invalid")
                        break
                    # Check if the user's balance is sufficient to send money
                    if amount > user_balance:
                        print("Your balance is insufficient to send money")
                    else:
                        # Deduct the sent amount from the user's balance
                        user_balance = user_balance - amount
                        print(f"You have successfully sent {amount}ghc. Your new balance is {user_balance}ghc")
                except ValueError:
                    print("Amount Invalid")

            # Option 3: Buy airtime
            if choice.strip() == "3":
                try:
                    print("You have chosen to buy airtime")
                    airtime = float(input("Enter airtime amount: "))
                    # Check if the entered airtime amount is negative
                    if airtime < 0:
                        print("Airtime amount invalid")
                        break
                    # Check if the user's balance is sufficient to purchase airtime
                    if airtime > user_balance:
                        print("Your balance is insufficient to purchase airtime")
                    else:
                        # Deduct the purchased airtime from the user's balance (at a 50% discount)
                        user_balance = user_balance - (airtime / 2)
                        print(f"You have purchased airtime worth {airtime}ghc at a 50% discount. Your new balance is: {user_balance}ghc")
                except ValueError:
                    print("Airtime amount invalid")

            # Option 'e': Exit the menu
            if choice.strip().lower() == "e":
                break

    # If the user enters 'q', exit the program
    elif code.strip().lower() == "q":
        break

    # If the user enters an incorrect code, display an error message
    else:
        print("Code incorrect, enter correct code to see menu or q to quit")