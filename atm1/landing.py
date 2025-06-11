import customers

# test 3 data dict

import customers


def check_pin():
    while True:
        inp_pin = input('Enter 4-digit code: ')

        for name, pin in customers.customers_data.items():
            if inp_pin == pin:
                print(f'Your pin {inp_pin} is correct, welcome {name}')
                return

        print(f'Your pin {inp_pin} is incorrect. Please try again.')


# Call the function
check_pin()

# test 2 function
# def    check_pin(inp_pin):
#     while True:
#         inp_pin=input('enter  digit code: ')
#         if inp_pin==customers.checkPin:
#             print(f'your pin {inp_pin} is Treu')
#             break
#         else:
#             print(f'your {inp_pin} is in correct.')
#
# check_pin(customers.checkPin)






#test1

# while True:
#     inp = input('enter 4 digit code: ')
#     if inp==customers.checkPin:
#         print(f'your entered code is:{inp} ,welcome to banks')
#         break
#     else:
#         print(f'your entered code is {inp} ,please try agin.')
#
#
