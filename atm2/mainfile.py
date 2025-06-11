import customers
from customers import customer_list
while True:
    entered_pin = input("Enter your PIN: ")

    for customer in customer_list:
        if customer.check_pin(entered_pin):
            print(f"welcome, {customer.get_name()}!")
            print(f"Your balance is: {customer.get_balance()}")

            deposit=float(input('ener new amount to deposit:'))
            new_balance = customer.get_balance() + deposit
            customer.set_balance(new_balance)
            print(f" new balance  to: {customer.get_balance()}")
            withdraw = float(input('ener new amount to withdraw:'))
            if withdraw>new_balance:
                print('you cant')
                continue
            else:
                print(f'{new_balance-withdraw} is your updatedd balance')



            break  # Exit for loop
    else:
        print(" PIN not correct. Try again.")
        continue

    break