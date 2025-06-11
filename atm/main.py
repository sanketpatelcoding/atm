# from users import users
#
# def verifypin():
#     while True:
#         try:
#             pin_input = int(input("Enter ATM pin: "))
#         except ValueError:
#             print("Please enter a 4-digit pin.")
#             continue
#
#         for userchk in users.values():
#             if userchk['pin'] == pin_input:
#                 print(userchk['name'], "banks")
#                 action=int(input("select option"))
#                 if action==1:
#                     print('balancechk')
#                     print(userchk['mainbalance'], "banks")
#                     if action == 2:
#                      print('withdraw')
#                     wAmount=float(input("enter withdraw amt :"))
#                     if wAmount>=userchk['mainbalance']:
#                         print(' cant withdraw')
#
#
#
#                 return
#         print("Incorrect pin. Please try again.")
#
# if __name__ == "__main__":
#     verifypin()
from users import users


def verifypin():
    while True:
        try:
            pin_input = int(input("Enter ATM pin: "))
        except ValueError:
            print("Please enter a 4-digit pin.")
            continue

        for userchk in users.values():
            if userchk['pin'] == pin_input:
                print(userchk['name'], "banks")
                action = int(input("Select option (1: Balance Check, 2: Withdraw) "))

                if action == 1:
                    print('Balance Check')
                    print(userchk['mainbalance'], "banks")

                elif action == 2:
                    print('Withdraw')
                    wAmount = float(input("Enter withdraw amount: "))
                    if wAmount > userchk['mainbalance']:
                        print(" not enough balance.")
                    else:
                        userchk['mainbalance'] -= wAmount
                        print(f"Withdrawal successful! New balance: {userchk['mainbalance']}")

                return

        print("Incorrect pin. Please try again.")


if __name__ == "__main__":
    verifypin()
