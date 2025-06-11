
class Customer:
    def __init__(self, name, pin, balance):
        self.__name = name
        self.__pin = pin
        self.__balance = balance
    def check_pin(self, entered_pin):
        return self.__pin == entered_pin

    def get_name(self):
        return self.__name

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        self.__balance = new_balance

customer_list = [
    Customer("sanket", "1234", 5000),
    Customer("chintu", "5678", 3000)
]


