# l = [1, "24", [3, 4, 5]]

# for i in l:
#     print(i*2)
    
# class Point01:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other_point):
#         new_x = self.x + other_point.x
#         new_y = self.y + other_point.y
#         return Point01(new_x, new_y)

# # Usage
# point1 = Point01(1, 2)
# point2 = Point01(3, 4)
# result = point1 + point2
# print("Result of addition:", result.__dict__)

# class Point02:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __sub__(self, other_point):
#         new_x = self.x - other_point.x
#         new_y = self.y - other_point.y
#         return Point02(new_x, new_y)

# # Usage
# point1 = Point02(5, 8)
# point2 = Point02(2, 3)
# result = point1 - point2
# print("Result of subtraction:", result.__dict__)

# class BinaryNumber:
#     def __init__(self, value):
#         self.value = value

#     def __rshift__(self, shift_by):
#         result = self.value >> shift_by
#         return BinaryNumber(result)

# # Usage
# binary_num = BinaryNumber(10)
# shifted_result = binary_num >> 2
# print("Result of right shift:", shifted_result.__dict__)

class Account:
    def __init__(self, account_no, user, amount):
        self.__account_no = account_no
        self.__user = user
        self.__amount = amount
        self.__transaction = []

    def get_account_no(self):
        return self.__account_no
    def get_user(self):
        return self.__user
    def get_amount(self):
        return self.__amount
    def get_transaction(self):
        return self.__transaction
    
    def __add__(self, other):
        if type(other) == int:
            self.__amount += other
        else:
            self.__amount += other.get_amount()
    def __sub__(self, other):
        if type(other) == int:
            self.__amount -= other
        else:
            self.__amount -= other.get_amount()
    def __rshift__(self, other):
        amount = other[1]
        target_account = other[2]
        self - amount
        target_account + amount
        
    def transfer(self, counter_no, amount, target_account):
        if amount < 0 or self.__amount < amount:
            return 'False'
        self >> (counter_no, amount, target_account)
        self.__transaction.append(Transaction('transfer', amount, self.__amount, target_account))
        target_account.get_transaction().append(Transaction('transfee', amount, target_account.get_amount(), self))

class SavingAccount(Account):

    interest_rate = 0.5
    type = "Saving"

    def __init__(self, account_no, user, amount):
        Account.__init__(self, account_no, user, amount)
        self.__card = []
        
    def add_card(self, card):
        super().add_card(card)
        self.__card.append(card)
        
    def get_card(self):
        return self.__card
    
card = SavingAccount(123, 'A', 1000)
print(card.get_card())

print(len('1-1101-12345-12-0'.split('-')))